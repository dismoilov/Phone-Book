from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # ...
    path('download/', views.download_xml, name='download_xml'),
    path('contacts.xml', views.view_xml, name='view_xml'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)