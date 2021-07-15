from django.urls import path, include
from rest_framework.routers import DefaultRouter
from poll import views
from account import views


router = DefaultRouter()
router.register(r'poll', views.PollViewSet)
router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]