from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, reset_password, verify

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegisterView.as_view(), name="register"),
    path("verify/<str:token>/", verify, name="verify"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path("profile/reset_password", reset_password, name="reset_password"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)