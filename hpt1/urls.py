from django.urls import path

from .views import index,form_creat,backend1,form_updat,backend2,backend3,reg

urlpatterns = [
     path('',index,name='index'),
    path ('form_creat/',form_creat,name='form_creat'),
    path('backend1/',backend1,name='backend1'),
    path('form_updat/<int:id>',form_updat,name='form_updat'),
    path('backend2/<int:id>',backend2,name='backend2'),
    path('backend3/<int:id>',backend3,name='backend3'),
    path('regester/',reg,name='reg')
]