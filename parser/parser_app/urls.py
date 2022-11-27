from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('child_questions/', views.child_questions, name='child_questions'),
]
