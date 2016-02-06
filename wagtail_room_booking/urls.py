from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from search import views as search_views
from room_booking import views

urlpatterns = [
    url(r'^booking_page/(?P<room_id>.*)/$', views.booking_page, name='booking_page'),
    url(r'^book/(?P<room_id>.*)/$', views.book, name='book'),
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url(r"^account/", include("account.urls")),
    url(r'^schedule/', include('schedule.urls')),
    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
