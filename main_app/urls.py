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
    path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update', views.AccessoryUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete', views.AccessoryDelete.as_view(), name='accessories_delete'),
    path('accessories/<int:violin_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
    path('accessories/<int:violin_id>/unassoc_accessory/<int:accessory_id>/', views.unassoc_accessory, name='unassoc_accessory'),
]
