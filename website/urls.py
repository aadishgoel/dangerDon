from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static 
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from music import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^albums/', views.AlbumList.as_view()),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)	