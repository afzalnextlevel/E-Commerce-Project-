from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('projects/', include('projects.urls')),
    path('Carts/', include('Carts.urls')),
    path('orders/', include('orders.urls')),
]

# Static and Media files serving during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
