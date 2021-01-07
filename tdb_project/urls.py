from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('company',views.company, name='company'),
    path('careers',views.career, name='careers'),
    path('team',views.team,name='team'),
    path('contact',views.contact,name='contact'),
    path('product',views.product,name='product'),
    path('form',views.applicant,name='form'),
    path('formsubmit',views.submit,name='submit')

]
