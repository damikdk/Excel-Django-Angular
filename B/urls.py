from web import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api
from web.api import OfficeFileResource

v1_api = Api(api_name='v1')
v1_api.register(OfficeFileResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
    url(r'^', views.onepage),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()