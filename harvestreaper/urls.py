"""harvestreaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin

from harvestreaper.views import HomePageView, LandingPageView, PrivacyPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('home', HomePageView.as_view(), name='home'),
    path('privacy', PrivacyPageView.as_view(), name='privacy'),

    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^harvest/', include('harvestreaper.harvest.urls')),

    path('admin/rq/', include('django_rq.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
