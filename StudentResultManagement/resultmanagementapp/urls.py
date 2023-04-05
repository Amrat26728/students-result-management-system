from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path("result", views.result, name="result"),
    path("courses", views.courses, name="courses"),
    path("login", views.loginform, name="loginform"),
    path("logout", views.logout_user, name="logout_user"),
    path("showresult", views.showresult, name="showresult")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
