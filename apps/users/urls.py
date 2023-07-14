from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from apps.users.views import (RegisterAPIView, LogoutAPIView, TeacherModelViewSet, TeacherDetailRetrieveAPIView,
                              RatingModelViewSet, SubscribeModelViewSet, WishListModelViewSet, TeacherSearchListAPIView)

routers = DefaultRouter()
routers.register('teachers', TeacherModelViewSet)
routers.register('rating', RatingModelViewSet)
routers.register('subscribe', SubscribeModelViewSet)
routers.register('wishlist', WishListModelViewSet)
routers.register('search_teacher', TeacherSearchListAPIView)

urlpatterns = [
    path('', include(routers.urls)),
    # User
    path('register', RegisterAPIView.as_view(), name='register'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    #  Teacher
    path('teacher_detail/<int:pk>', TeacherDetailRetrieveAPIView.as_view(), name='teacher'),

]
