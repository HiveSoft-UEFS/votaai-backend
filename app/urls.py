from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

from .views import user_view, vote_view, poll_view
from .views import LogoutView

router = routers.DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='User')
router.register(r'votes', vote_view.VoteViewSet, basename='Vote')
router.register(r'polls', poll_view.PollViewSet, basename='Polls')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    # rotas do logout
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
