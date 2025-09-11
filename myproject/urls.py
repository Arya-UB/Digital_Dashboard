"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from myapp.views import LoginView,LogoutView,AdduploadView,UploadReadView,UpdateView,DeleteView,DetailView,Home,AdminRegisterView,admin_dashboard_view,Intro,AnnouncementView,AnnounceReadView,AnounceUpdateView,AnDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('adminregister/',AdminRegisterView.as_view(),name='adminsignin'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('upload/',AdduploadView.as_view(),name='create'),
    path('viewuploads/',UploadReadView.as_view(),name='uploadlist'),
    path('uploadsupdate/<int:pk>',UpdateView.as_view(),name='update'),
    path('uploaddelete/<int:pk>',DeleteView.as_view(),name='delete'),
    path('detail/<int:id>/',DetailView.as_view()),
    path('',Home.as_view()),
    path('dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('home/',Intro.as_view(),name='home'),
    path('announcement/',AnnouncementView.as_view(),name='announcement'),
    path('anread/',AnnounceReadView.as_view(),name='read'),
    path('Anuploadsupdate/<int:pk>',AnounceUpdateView.as_view(),name='anupdate'),
    path('Anddelete/<int:pk>',AnDeleteView.as_view(),name='andelete'),
    
] 

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
