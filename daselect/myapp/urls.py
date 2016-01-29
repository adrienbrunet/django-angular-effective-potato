from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r'children', views.ChildViewSet, base_name='child')


urlpatterns = [
    url(r'^$', views.ChildList.as_view(), name='home'),
    url(r'edit/(?P<pk>\d+)$', views.ChildEdit.as_view(), name='edit'),
    url(r'^api/', include(router.urls))
]
