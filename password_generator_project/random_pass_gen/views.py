from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('specialcharacter'):
        characters.extend(list('!@#$%^&*()'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'Show_password.html', {'password':thepassword})