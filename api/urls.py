from django.urls import path

from .views import *


urlpatterns = [
    # topic
    path('topic/', TitleListView.as_view()),
    path('topic/<int:pk>/', TitleDetailView.as_view()),
]