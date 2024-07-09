from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import user_view, vote_view, poll_view
from .views.customTokenObtainPairView import CustomTokenObtainPairView


router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='User')
router.register(r'votes', vote_view.VoteViewSet, basename='Vote')
router.register(r'polls', poll_view.PollViewSet, basename='Polls')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('polls/search/s', poll_view.PollViewSet.as_view({'get': 'search'}), name='poll-search'),
]
