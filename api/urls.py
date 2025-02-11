from django.urls import path

from .views import *


urlpatterns = [
    # topic
    path('topic/', TitleListView.as_view()),
    path('topic/<int:pk>/', TitleDetailView.as_view()),

    # comment
    path('comment/', CommentListView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),

    # user
    path('user/<int:pk>/', UserDetailView.as_view())
]