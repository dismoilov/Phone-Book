from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import incoming_call, outgoing_call, missed_call

urlpatterns = [
    path('api/call/incoming/', incoming_call, name='incoming_call'),
    path('api/call/outgoing/', outgoing_call, name='outgoing_call'),
    path('api/call/missing/', missed_call, name='outgoing_call'),
    path('download/', views.download_xml, name='download_xml'),
    path('contacts.xml', views.view_xml, name='view_xml'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
