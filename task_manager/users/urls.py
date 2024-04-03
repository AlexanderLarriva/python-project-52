from django.urls import path
from task_manager.users import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    # path('<int:user_id>/edit/', edit_user, name='edit_user'),
    # path('<int:user_id>/delete/', delete_user, name='delete_user'),
    
]