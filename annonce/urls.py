# from django.conf.urls import url
from django.urls import re_path
from django.contrib import admin
from django.urls import path
from . import views
from .views import VerificationView
urlpatterns = [
    path('creer-annonce', views.create_annonce, name='creer-annonce'),
    path('register', views.inscriptionPage, name='register'),
    path('login-annonce', views.login_user, name='login-annonce'),
    path('logout-annonce', views.logout_annonce, name='logout-annonce'),
    path('logged-annonce', views.logged_annonce, name='logged-annonce'),
    path('annonce-profil', views.profile_annonce, name='annonce-profil'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('annonce/gerer-annonce', views.gerer_annonce, name='gerer-annonce'),
    path('annonce/dashboard/<str:pk>', views.dashboard_view, name='dashboard-annonce'),
    path('annonce/dashboard/description/<str:pk>/', views.description_view, name='dashboard-description'),
    path('annonce/dashboard/dureeLocation/<str:pk>/', views.dureeLocation_view, name='dashboard-dureelocation'),
    path('annonce/dashboard/equipment/<str:pk>/', views.equipment_view, name='dashboard-equipment'),
    path('annonce/dashboard/loyer/<str:pk>/', views.loyer_view, name='dashboard-loyer'),
    path('annonce/dashboard/photos/<str:pk>/', views.image_view, name='dashboard-image'),
    path('annonce/dashboard/photos/delete/<str:pk>/', views.delete_image, name='delete-image'),
    path('annonce/dashboard/calendrier/<str:pk>/', views.calendrier, name='dashboard-calendrier'),
    path('annonce/dashboard/calendrier/create/<str:pk>/', views.create_calendrier, name='create-calendrier'),
    path('annonce/dashboard/calendrier/edit/<str:pk>/', views.edit_calendrier, name='calendrier-edit'),
    path('annonce/dashboard/calendrier/delete/<str:pk>/', views.delete_calendrier, name='calendrier-delete'),
    path('annonce/dashboard/calendrier/delete_confirm/<str:pk>/', views.delete_calendrier_confirm, name='calendrier-delete-confirm'),
    path('annonce/dashboard/conditions/<str:pk>/', views.condition_view, name='dashboard-condition'),
    path('annonce/dashboard/diagnostic/<str:pk>/', views.diagnsotic_view, name='dashboard-diagnostic'),
    path('annonce/dashboard/coordonnee_user/<str:pk>/', views.user_view_dashboard, name='dashboard-usercoord'),
    path('annonce/dashboard/verif/<str:pk>/', views.verification_view, name='dashboard-verif'),
    path('annonce/dashboard/sign/get_signing_url', views.embeded_signing_ceremony, name='get_signing_url'),
    path('annonce/dashboard/sign/get_access_code', views.get_access_code, name='get_access_code'),
    path('annonce/dashboard/sign/auth_login', views.auth_login, name='auth_login'),
    #url(r'^sign_completed/$', views.sign_complete, name='sign_completed'),
]