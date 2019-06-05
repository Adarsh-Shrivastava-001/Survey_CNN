"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


app_name="Survey"
from django.contrib import admin
from django.urls import path, include
from .views import Home, Que, next_que, start, End, result



urlpatterns = [

    path('', Home.as_view(), name= 'home'),
    path('<int:mid>/<int:num>', Que.as_view(), name = 'que'),
    path('next/<int:mid>/<int:num>', next_que, name = 'nextque'),
    path('start/', start, name='start'),
    path('end/', End.as_view(), name='end'),
    path('adarsh/results/', result, name='result')

]
