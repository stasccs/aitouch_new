from django.shortcuts import render, get_object_or_404
from django import forms
from django.core.paginator import Paginator
from .forms import CreateForm
from .models import Blog
from django.core.files.storage import FileSystemStorage
from time import strftime, localtime


def check_user(request):
    global user
    if 'user' in request.session:
        user = request.session['user']
    else:
        user = 'Гость'
    context = {
        'user': user
    }


# Представление для загрузки страницы новостей сайта
def blog(request):
    check_user(request)
    posts_x = Blog.objects.all()
    paginator = Paginator(posts_x, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


# Представление для загрузки страницы добавления новостей сайта
def create(request):
    if request.method == 'POST':
        check_user(request)
        title = request.POST.get('title')
        annotation = request.POST.get('annotation')
        content = request.POST.get('content')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        file_url = fs.url(filename)

        publish = strftime('%Y-%m-%d %H:%M:%S', localtime())


        post = Blog(
            title=title, annotation=annotation,
            content=content,
            photo=file_url, publish=publish,

        )
        post.save()

        message = 'Новость успешно добавлена'
        color = 'green'
        context = {
            'user': user,
            'color': color,
            'message': message
        }
        return render(request, 'blog/create_res.html', context)
    else:
        check_user(request)
        form = CreateForm()
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'blog/create.html', context)


# Представление для загрузки страницы удаления новостей сайта
def delete(request, id):
    if request.method == 'POST':
        check_user(request)
        post = Blog.objects.get(id=id)
        post.delete()
        context = {
            'user': user,
            'message': 'Новость успешно удалена'
        }
        return render(request, 'blog/delete_res.html', context)
    else:
        check_user(request)
        post = Blog.objects.get(id=id)
        context = {
            'user': user,
            'post': post
        }
        return render(request, 'blog/delete.html', context)


# Представление для загрузки страницы просмотра отдельной новости сайта
def single(request, id):
    check_user(request)
    post = Blog.objects.get(id=id)
    context = {
        'user': user,
        'post': post
    }
    return render(request, 'blog/single.html', context)


# Представление для загрузки страницы редактирования новостей сайта
def edit(request, id):
    if request.method == 'POST':
        check_user(request)
        post = Blog.objects.get(id=id)
        form = CreateForm(request.POST)
        post.title = request.POST.get('title')
        post.annotation = request.POST.get('annotation')
        post.content = request.POST.get('content')
        post.link = request.POST.get('link')

        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        post.file_url = fs.url(filename)

        post.publish = strftime('%Y-%m-%d %H:%M:%S', localtime())
        post.status = 'Отредактирована'
        post.save()

        message = 'Новость успешно отредактирована'
        color = 'green'
        context = {
            'user': user,
            'post': post,
            'form': form,
            'color': color,
            'message': message
        }
        return render(request, 'blog/edit_res.html', context)
    else:
        check_user(request)
        post = Blog.objects.get(id=id)
        form = CreateForm(initial={'title': post.title, 'annotation': post.annotation, 'content': post.content, 'link': post.link})
        context = {
            'user': user,
            'form': form,
            'post': post,
        }
        return render(request, 'blog/edit.html', context)


