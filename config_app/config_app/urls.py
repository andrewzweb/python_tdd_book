from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from lists import views as list_views
from lists import urls as list_urls 

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^lists/', include(list_urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
