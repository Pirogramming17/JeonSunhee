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
    path('devList', views.devtoolList, name="devtoolList"),
    path('devtoolCreate', views.devtoolCreate, name="devtoolCreate"),
    path('devtool/devtoolUpdate/<int:id>', views.devtoolUpdate, name="devtoolUpdate"),
    path('devtool/<int:id>',views.devtoolDetail, name="devtoolDetail"),
    path('devtoolDelete/<int:id>', views.devtoolDelete, name="devtoolDelete"),
    path('ideaDelete/<int:id>', views.ideaDelete, name="ideaDelete"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)