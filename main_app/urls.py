from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('violins/',views.violins_index, name='index'),
    path('violins/<int:violin_id>/', views.violins_detail, name='detail'),
    path('violins/create/', views.ViolinCreate.as_view(),name='violins_create'),
    path('violins/<int:pk>/update/', views.ViolinUpdate.as_view(), name='violins_update'),
    path('violins/<int:pk>/delete/', views.ViolinDelete.as_view(), name='violins_delete'),
    path('violins/<int:violin_id>/add_tuneup/', views.add_tuneup, name='add_tuneup'),
]
