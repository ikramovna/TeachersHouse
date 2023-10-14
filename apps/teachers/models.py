from django.db.models import (Model, CharField, EmailField, TextChoices, IntegerField, TextField, ImageField,
                              ForeignKey, PositiveIntegerField, DateTimeField, CASCADE, ManyToManyField)

from apps.teachers.models import Subject


class Teacher(Model):
    full_name = CharField(max_length=50)
    email = EmailField()
    address = CharField(max_length=100)

    class Status(TextChoices):
        VERIFIED = 'verified', 'Verified'
        NOT_VERIFIED = 'not verified', 'Not Verified'

    status = CharField(max_length=15, choices=Status.choices)

    class Gender(TextChoices):
        FEMALE = 'female', 'Female'
        MALE = 'male', 'Male'

    gender = CharField(max_length=15, choices=Gender.choices)
    teaching_language = CharField(max_length=50)
    teaching_subject = CharField(max_length=50)
    experience = IntegerField()
    bio = TextField()
    image = ImageField(upload_to='teachers/image/')
    subject = ManyToManyField(Subject)



class Rating(Model):
    user = ForeignKey('auth.User', CASCADE)
    teacher = ForeignKey('Teacher', CASCADE)
    rating = PositiveIntegerField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user



class Subscribe(Model):
    email = EmailField()
    subscribe_at = DateTimeField(auto_now_add=True)


class Wishlist(Model):
    product = ForeignKey('Teacher', CASCADE)
    user = ForeignKey('auth.User', CASCADE)
    created_at = DateTimeField(auto_now=True)


class Subject(Model):
    name = CharField(max_length=255)

class Subscribe(Model):
    email = EmailField()
    subscribe_at = DateTimeField(auto_now_add=True)

class Rating(Model):
    user = ForeignKey('auth.User', CASCADE)
    teacher = ForeignKey('Teacher', CASCADE)
    rating = PositiveIntegerField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
