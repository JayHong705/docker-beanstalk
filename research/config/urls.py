from django.urls import path, include
from rest_framework.routers import DefaultRouter
from poll import views

router = DefaultRouter()
router.register(r'poll', views.PollViewSet)

urlpatterns = [
    path('', include(router.urls)),
]