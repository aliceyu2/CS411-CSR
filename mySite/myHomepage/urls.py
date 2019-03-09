from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
	path('admin/', admin.site.urls),
	path('myHomepage/', include(myHomepage.urls)),
	path('', RedirectView.as_view(url='/myHomepage/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
