from . import views
from django.conf.urls import url

urlpatterns = [
    # url(r'^1/',views.index,name='index'),
    url(r'^$',views.page1,name='page1'),
    url(r'^2/',views.page2,name='page2'),
    url(r'^3/',views.page3,name='page3')
]