from django.shortcuts import render
from django.views import View
# from django.utils.translation import gettext as _


class IndexUser(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/index.html')