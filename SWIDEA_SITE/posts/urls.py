import imp
from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "posts"

urlpatterns = [
    path('', views.main, name="main"),
    path('ideaCreate',views.ideaCreate, name="ideaCreate"),
    path('post/idea/<int:id>',views.ideaDetail, name="ideaDetail"),
    path('post/ideaUpdate/<int:id>', views.ideaUpdate, name="ideaUpdate"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)