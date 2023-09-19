from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('', views.home, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('donation-listing/', views.donation_listing, name='donation_listing'),
    path('blog/', views.blog, name='blog'),
    path('events/', views.events, name='events'),
    path('faq/', views.faq, name='faq'),
    path('service/', views.service, name='service'),
    path('volunteers/', views.volunteers, name='volunteers'),
    path('donation/', views.donation_details, name='donation_details'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('gallery/', views.gallery, name='gallery'),
    path('join_volunteers/', views.join_volunteers, name='join_volunteers'),
    path('ajax_gallery/', views.gallery_ajax, name='ajax_gallery'),
    path('volunteers_ajax/', views.volunteers_ajax, name='volunteers_ajax'),
    path('callback/', views.callback, name='callback'),
    path('login/', views.login, name='login'),
     path('logout/', views.user_logout, name='logout'),
     path('donors_list/', views.donors_list, name='donors_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)