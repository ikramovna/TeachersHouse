from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import (RegisterAPIView, LogoutAPIView)

routers = DefaultRouter()
# routers.register('orders/', OrderModelViewSet, 'orders')
urlpatterns = [
    path('', include(routers.urls)),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]
