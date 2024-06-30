from django.urls import include, path
from rest_framework import routers

from .views import user_view, vote_view

router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='User')
router.register(r'votes', vote_view.VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]