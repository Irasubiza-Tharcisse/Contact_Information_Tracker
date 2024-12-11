from django.urls import path
from . import views
urlpatterns =[
  path('all_users',views.all_users_view,name="all_users"),
  path('edit_user/<int:user_id>',views.edit_user_view,name="edit_user"),
  path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
]