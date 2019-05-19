"""gdrive_to_commons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from gdrive_to_commons.views import UserLogoutView
from uploader.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    url(r"^upload/", include("uploader.urls")),
    path("admin/", admin.site.urls),
    url(r"^api-auth/", include("rest_framework.urls")),
    url(r"oauth/", include("social_django.urls", namespace="social")),
    url(r"logout/", UserLogoutView.as_view(), name="logout"),
] + static(settings.STATIC_URL_DEPLOYMENT, document_root=settings.STATIC_ROOT)
