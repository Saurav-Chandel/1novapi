
from django.contrib import admin
from django.urls import path
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/signup/", RegisterView.as_view(), name="signup"),
    path("auth/user/", GetUserDetail.as_view(), name="user_detail"),
    path("auth/post/", RegisterPost.as_view(), name="user_post"),
    path("auth/view/", PostView.as_view(), name="view_post"),
    # path("auth/otpgenerate/", OtpGenerate.as_view(), name="otp_generate"),
    path("auth/otpverify/", Otp_Verification.as_view(), name="otp_generate"),
    path("auth/publication/", RegisterPublication.as_view(), name="register_publication"),
]
