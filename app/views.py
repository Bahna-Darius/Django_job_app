from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader


job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]


def hello(request):
    lista = ["alpha", "beta"]
    is_authenticated = False
    context = {
        "name": "Django",
        "age": 30,
        "first_list": lista,
        "is_authenticated": is_authenticated
    }

    return render(request, "app/hello.html",context)


def job_list(request):
    context = {
        "job_title_list": job_title
    }

    return render(request, "app/index.html", context)


# Acest prim parametru din functii request el este folosit ca responsabil pentru a oferi informatia
def job_detail(request, id):
    print(type(id))

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {
            "job_title": job_title[id],
            "job_description": job_description[id]
        }
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
