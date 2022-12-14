"""project_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from project_app import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.UserCreateView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('create/', views.CreateTripView.as_view(), name='create'),
    path('update/<int:trip_id>/',views.TripUpdateView.as_view(), name='update'),
    path('delete/<int:trip_id>/',views.TripDeleteView.as_view(), name='delete'),
    path('list/', views.TripListView.as_view(), name='explore'),
    path('list/<int:trip_id>/',views.TripDetailView.as_view(),name='explore each'),
    path('profile/',views.UsersProfileView.as_view(), name='all users'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='profiles'),
    path('profile/<int:user_id>/update/', views.UserProfileUpdateView.as_view(), name='update profiles'),
    path('users/',views.UsersView.as_view(), name='all users'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),



    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)