from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('i18n/', include('django.conf.urls.i18n')),

                  # The Django admin is not officially supported; expect breakage.
                  # Nonetheless, it's often useful for debugging.

                  path('admin/', admin.site.urls),
                  path(r'^checkout/paypal/', include('paypal.express.urls')),
                  path('', include(apps.get_app_config('oscar').urls[0])),
                  path('auth_accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
