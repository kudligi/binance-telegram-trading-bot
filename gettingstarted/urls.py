from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import webhook.views
import telegram.views
import oms.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("ping/", webhook.views.ping),
    path('alert/', webhook.views.alert, name="alert"),
    path('hook/', telegram.views.talkin_to_me_bruh, name="bot-hook"),
    path('binance/', include('oms.urls'))
]
