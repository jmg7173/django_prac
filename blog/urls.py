from django.conf.urls import urls
from . import view


urlpatterns = [
    url(r'^$', view.post_list, name='post_list'),
]
