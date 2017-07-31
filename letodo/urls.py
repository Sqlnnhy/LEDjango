from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from letodo import views

urlpatterns = [
    url(r'^index', views.index),

]
urlpatterns = format_suffix_patterns(urlpatterns)
