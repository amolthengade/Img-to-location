from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.imageinfo, name='imageinfo'),  # Adjust according to your main view
    path('map/<str:latitude>/<str:longitude>/', views.imap, name='imap'),
    path('text', views.extract_text_with_easyocr, name='text'),
]
