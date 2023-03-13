from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("child_questions/", views.child_questions, name="child_questions"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("support/", views.support, name="support"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("quiz_create/", views.quiz_create, name="quiz_create"),
]
""" if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """
