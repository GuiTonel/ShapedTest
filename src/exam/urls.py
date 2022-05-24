from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("exams", views.ExamView, basename="exams")

urlpatterns = [
    path("", include(router.urls)),
]
