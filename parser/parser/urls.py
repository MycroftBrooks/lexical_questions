from django.contrib import admin
from django.urls import include, path
from theme.views import change_theme

urlpatterns = [
    path("admin/", admin.site.urls),
    path("switch-theme/", change_theme, name="change_theme"),
    path("", include("parser_app.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
