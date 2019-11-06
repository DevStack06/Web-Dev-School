from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
urlpatterns = [
    #extras not required databases
    path('admissioninfo/',views.admissionInfo.as_view(),name='admissioninfo'),
    path('labs/',views.labs.as_view(),name='labs'),
    path("about/",views.about.as_view(),name="about"),
    path("mission/",views.mission.as_view(),name="mission"),
    path("principal/",views.principal.as_view(),name="principal"),
    
    path("yoga/",views.yoga.as_view(),name="yoga"),
    path("playground/",views.playground.as_view(),name="playground"),
    path("hostel/",views.hostel.as_view(),name="hostel"),
    path("opengym/",views.opengym.as_view(),name="opengym"),
    path("mess/",views.mess.as_view(),name="mess"),
    path("smartclass/",views.smartclass.as_view(),name="smartclass"),
    
    path("",views.index.as_view(),name="index"),
    path("contact_us/",views.contact_us.as_view(),name="contact_us"),

    path("faculty/add/", login_required(views.addFaculty.as_view()) ,name='addFaculty'),
    path("faculty/update/<int:id>/",login_required(views.updateFaculty.as_view()) ,name='updateFaculty'),
    path("faculty/delete/<int:id>/", login_required(views.addFaculty.delete) ,name='deleteFaculty'),
    path("faculty/",views.listFaculty.as_view(),name="listFaculty"),
    path("staff/",views.listStaff.as_view(),name="listStaff"),

    path("SAL/",views.listStuAchiev.as_view(),name="listStuAchieve"),
    path('albums/', views.listAlbum.as_view() ,name='listAlbum'),
    path("album/<int:pk>/", views.listPhoto.as_view() ,name='listPhoto'),
    path('review/',views.listReview.as_view(),name='listReview'),


    path("SAL/add/",login_required( views.addStuAchive.as_view()),name="addStuAchive"),
    path("albums/add/",login_required( views.addAlbum.as_view()) ,name='addAlbum'),
    path("album/update/<int:id>/",login_required( views.updateAlbum.as_view()) ,name='updateAlbum'),
    path("album/delete/<int:id>/",login_required( views.deleteAlbum.as_view()) ,name='deleteAlbum'),    
    path("album/<int:pk>/add",login_required( views.addPhoto.as_view()) ,name='addPhoto'),
    path("album/<int:pk>/delete/<int:picid>/", login_required(views.deletePhoto.as_view()) ,name='deletePhoto'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#+urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    

    