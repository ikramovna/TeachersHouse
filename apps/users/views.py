from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import Teacher, Rating, Subscribe, Wishlist
from apps.users.serializers import (TeacherModelSerializer, TeacherDetailModelSerializer, RatingModelSerializer,
                                    SubscriptionSerializer, WishListModelSerializer)
from apps.users.services import register_service, reset_password_service, reset_password_confirm_service


# User/Register API
class RegisterAPIView(APIView):
    def post(self, request):
        response = register_service(request.data)
        if response['success']:
            return Response(status=201)
        return Response(response, status=405)


#  User/Reset Password API
class ResetPasswordAPIView(APIView):
    def post(self, request):
        responce = reset_password_service(request)
        if responce['success']:
            return Response({'message': 'sent'})
        return Response(responce, status=404)


# User/Reset Password Confirm API

class PasswordResetConfirmAPIView(APIView):

    def post(self, request, token, uuid):
        response = reset_password_confirm_service(request, token, uuid)
        if response['success']:
            return Response({'message': 'Password changed'})
        return Response(response, status=400)


# User/Logout API
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = RefreshToken(request.user)
        token.blacklist()
        return Response(status=200)


#  Teacher/List API

class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    # pagination_class = PageNumberPagination
    permission_classes = ()


#  Teacher/Detail API

class TeacherDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailModelSerializer
    permission_classes = ()


# Rating API
class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer


# Subscribe API
class SubscribeModelViewSet(ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscriptionSerializer


#  Wishlist API
# WishList
class WishListModelViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishListModelSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).filter(product_id=kwargs.get('pk'), user=request.user)
        instance = get_object_or_404(queryset)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


#  Search for Teachers API
class TeacherSearchListAPIView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['teaching_subject', 'teaching_language']
    permission_classes = [AllowAny]
