from django.urls import path
from app import views

urlpatterns = [
    path("Job/<int:id>", views.job_detail),
    path("hom", views.home_page, name='home'),
]
