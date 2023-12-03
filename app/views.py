from django.shortcuts import render, redirect
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1>Home Page</h1>")


def job_detail(request, id: int):
    if id == 0:
        return redirect("home")

    messaje = f"Job detail page {id}!"
    return HttpResponse(messaje)


