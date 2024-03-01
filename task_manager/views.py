from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _


# def index(request):
    # context = {
    #     'hello': _('Hello!')
    # }
    # return render(request, 'index.html', context)


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
