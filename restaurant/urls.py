from django.urls import path, include
from . import views
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]