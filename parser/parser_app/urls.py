from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("child_questions/", views.child_questions, name="child_questions"),
    path("register/", views.register, name="register"),
    # path("login/", views.login, name="login"),
    path("logout", views.logout_user, name="logout"),
]
""" if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) """
