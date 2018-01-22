from django.conf.urls import url
from . import views

def test(request):
    print "app level"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.process),
    url(r'^result$', views.display_result),
]