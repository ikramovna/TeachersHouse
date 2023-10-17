from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from apps.teachers.models import Teacher, Rating, Subscribe, Wishlist
from apps.teachers.serializers import (TeacherModelSerializer, 
                                       TeacherDetailModelSerializer,
                                       RatingModelSerializer,
                                       SubscriptionSerializer, 
                                       WishListModelSerializer)


class TeacherModelViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    # pagination_class = PageNumberPagination
    permission_classes = ()



class TeacherDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailModelSerializer
    permission_classes = ()



class RatingModelViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer



class SubscribeModelViewSet(ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscriptionSerializer



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


class TeacherSearchListAPIView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['teaching_subject', 'teaching_language']
    permission_classes = [AllowAny]


class TeacherListByTopicAPIView(ListAPIView):
    serializer_class = TeacherModelSerializer

    def get_queryset(self):
        teaching_subject = self.request.query_params.get('topic', '')
        return Teacher.objects.filter(topics__name__iexact=teaching_subject)
