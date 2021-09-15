from django.shortcuts import render, redirect, reverse


def home(request):
    return render(request, 'base.html')
