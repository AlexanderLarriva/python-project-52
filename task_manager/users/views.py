from django.shortcuts import render
from django.views import View
from .models import CustomUser
# from django.utils.translation import gettext as _


# class IndexUser(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'users/user_list.html')

class UserList(View):
    
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(request, 'users/user_list.html', {'users': users})
