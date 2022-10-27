from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.urls import path, include  # add this
from .views import ProfileList, ProfileDetail, UserDataList, UserDataDetail

urlpatterns = [
    path('profile/', ProfileList.as_view()),
    path('profile/<int:pk>', ProfileDetail.as_view()),
    path('userdata/', UserDataList.as_view()),
    path('userdata/<int:pk>', UserDataDetail.as_view()),
]
