from django.urls import path, include
from .views import RegisterApi

urlpatterns = [
    path('auth_login/', include('dj_rest_auth.urls')),
    # path('auth_register/', include('dj_rest_auth.registration.urls')),
    path('register/', RegisterApi.as_view())
]