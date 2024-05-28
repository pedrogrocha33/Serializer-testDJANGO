from django.urls import path
from users.views import (
    UserAPIView,
    LoginView,
    UserConfirmationRequestCodeView,
    UserConfirmationRequestEmailView,
    UserMeAPIVIew,
)


urlpatterns = [
    path("users/", UserAPIView.as_view(), name="users"),
    path("user/me/", UserMeAPIVIew.as_view(), name="user_me"),
    path("token/", LoginView.as_view(), name="token"),
    path(
        "confirmation/send_email/",
        UserConfirmationRequestEmailView.as_view(),
        name="confirmation_email",
    ),
    path(
        "confirmation/send_code/",
        UserConfirmationRequestCodeView.as_view(),
        name="confirmation_code",
    ),
]
