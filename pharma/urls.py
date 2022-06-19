from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),

    url(r'^medform/', views.medform, name="medform"),
    url(r'^medforminsert/', views.medforminsert, name="medforminsert"),
    url(r'^medformupdate(?P<foo>[0-9]+)/', views.medformupdate, name="medformupdate"),
    url(r'^medformview(?P<foo>[0-9]+)/', views.medformview, name="medformview"),
    url(r'^medformdelete(?P<foo>[0-9]+)/', views.medformdelete, name="medformdelete"),
    url(r'^medtable/', views.medtable, name='medtable'),
    
    url(r'^custform/', views.custform, name="custform"),
    url(r'^custforminsert/', views.custforminsert, name="custforminsert"),
    url(r'^custformupdate(?P<foo>[0-9]+)/', views.custformupdate, name="custformupdate"),
    url(r'^custformview(?P<foo>[0-9]+)/', views.custformview, name="custformview"),
    url(r'^custformdelete(?P<foo>[0-9]+)/', views.custformdelete, name="custformdelete"),
    url(r'^custtable/', views.custtable, name='custtable'),

    url(r'^purchaseform/', views.purchaseform, name="purchaseform"),
    url(r'^purchaseforminsert/', views.purchaseforminsert, name="purchaseforminsert"),
    url(r'^purchaseformupdate(?P<foo>[0-9]+)/', views.purchaseformupdate, name="purchaseformupdate"),
    url(r'^purchaseformview(?P<foo>[0-9]+)/', views.purchaseformview, name="purchaseformview"),
    url(r'^purchaseformdelete(?P<foo>[0-9]+)/', views.purchaseformdelete, name="purchaseformdelete"),
    url(r'^purchasetable/', views.purchasetable, name='purchasetable')
]
