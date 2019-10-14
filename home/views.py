from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect, BadHeaderError
from django.core.mail import send_mail


# Представление для загрузки главной страницы сайта
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


def thanks(request):

    return render(request, 'home/thanks.html')


# Функция формы обратной связи
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = 'New message from A.I.Touch'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            full_message = f" Name: {name}\n Email: {email} \n Message: {message}"
            recepients = ['office@aitouch.pl']

            try:
                send_mail(subject, full_message, 'office@aitouch.pl', recepients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            return HttpResponseRedirect('/home/thanks')

    else:
        form = ContactForm()
    # Выводим форму в шаблон
    return render(request, 'home/contact.html', {'form': form})