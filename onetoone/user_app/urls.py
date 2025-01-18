from django.urls import path
from . import views

urlpatterns = [
    path('ucreate/', views.user_create_view, name = 'ucreate_url'),
    path('uretrive/', views.user_retrive_view, name='uretrive_url'),
    path('uupdate/<pk>/', views.user_update_view, name='uupdate_url'),
    path('udelete/<pk>/', views.user_delete_view, name='udelete_url'),

    path('pcreate/', views.profile_create_view, name = 'pcreate_url'),
    path('pretrive/', views.profile_retrive_view, name='pretrive_url'),
    path('pupdate/<pk>/', views.profile_update_view, name='pupdate_url'),
    path('pdelete/<pk>/', views.profile_delete_view, name='pdelete_url')

]