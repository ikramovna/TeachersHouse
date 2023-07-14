from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from root.settings import MEDIA_URL, MEDIA_ROOT
from root.swagger import swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),


              ] + swagger_urls + static(MEDIA_URL, document_root=MEDIA_ROOT)
