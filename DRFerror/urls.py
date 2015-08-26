from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from .views import StartupViewSet

router = routers.DefaultRouter()
router.register(r'startups', StartupViewSet)

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(include(router.urls)))
)
