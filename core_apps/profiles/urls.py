from django.urls import path
from .views import (AvatarUploadView, ProfileListAPIView, ProfileDetailAPIView,
                    ProfileUpdateAPIView, NonTenantProfilesListAPIView)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="profile-list"),
    path("non-tenant-profiles/", NonTenantProfilesListAPIView.as_view(),
         name="non-tenant-profiles"),
    path("user/my-profile/", ProfileDetailAPIView.as_view(), name="profile-detail"),
    path("user/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    path("user/avatar/", AvatarUploadView.as_view(), name="avatar-upload"),
]
