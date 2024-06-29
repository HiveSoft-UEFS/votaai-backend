from django.urls import path
from .views.userView import create_user
from .views.voteView import VoteDetailView

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('vote/<str:hash>/', VoteDetailView.as_view(), name='vote-detail'),
]