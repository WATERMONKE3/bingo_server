"""bingo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('bingo', views.bingo, name='bingo'),
    path('bingo/save_selected_number/', views.save_selected_number, name='save_selected_number'),
    path('bingo/new_bingo_game/', views.new_bingo_game, name='new_bingo_game'),
    path('bingo/check_selection/', views.check_selection, name='check_selection'),
    path('raffle', views.raffle, name='raffle'),
    path('save_winner', views.save_winner, name='save_winner'),
    path('import_raffle_entries/', views.import_raffle_entries, name='import_raffle_entries'),
]
