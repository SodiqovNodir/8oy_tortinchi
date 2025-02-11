from django.urls import path

from .views import *


urlpatterns = [

    path('title/', TitleListView.as_view()),
    path('title/<int:pk>/', TitleDetailView.as_view()),
]