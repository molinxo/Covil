
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('gear/', views.gear, name='gear'),

    # ➜ AQUI! Rota para visualizar um post individual
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
]

