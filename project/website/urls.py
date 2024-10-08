from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403

handler403 = 'your_app.views.custom_permission_denied_view'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('about-me/', views.about_me, name='about_me'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('record-payment/<int:appointment_id>/', views.record_payment, name='record_payment'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('add-availability/', views.add_availability, name='add_availability'),
    path('delete-availability/<int:availability_id>/', views.delete_availability, name='delete_availability'),
    path('appointment/', views.appointment, name='appointment'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('get-availabilities/', views.get_availabilities, name='get_availabilities'),
    path('update-google-meet-link/<int:appointment_id>/', views.update_google_meet_link, name='update_google_meet_link'),

]    