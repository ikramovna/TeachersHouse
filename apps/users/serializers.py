from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from apps.users.models import Teacher, Rating, Subscribe, Wishlist




class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = 'full_name', 'bio'


class TeacherDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class RatingModelSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class WishListModelSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
