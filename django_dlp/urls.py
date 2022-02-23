from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from slack_events_test import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('slack_events/', include(urls), name="slack_events"),
]
