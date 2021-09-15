from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import SearchEngine
from django.template.loader import render_to_string
import datetime
import json
from datetime import datetime, timedelta


class HomeListView(ListView):
    model = User
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.all()
        context['keyword'] = SearchEngine.objects.all()
        new_format = "%Y-%m-%d"
        yesterday = datetime.today() - timedelta(days=1)
        week = datetime.today() - timedelta(days=7)
        month = datetime.today() - timedelta(days=30)
        context['yesterday'] = yesterday.strftime(new_format)
        context['week'] = week.strftime(new_format)
        context['month'] = month.strftime(new_format)
        print(context['user'])
        return context


def search(request):
    now = datetime.today()
    new_format = "%Y-%m-%d"
    now = now.strftime(new_format)
    filter_keyword = request.GET.getlist('keyword[]')
    filter_user = request.GET.getlist('user[]')
    filter_time = request.GET.get('time[]')
    all_search = SearchEngine.objects.all()
    if len(filter_keyword) > 0:
        all_search = SearchEngine.objects.filter(keywords__in=filter_keyword)
    if len(filter_user) > 0:
        all_search = all_search.filter(user__username__in=filter_user)
    if filter_time is not None:
        all_search = SearchEngine.objects.filter(search_date__gte=filter_time, search_date__lte=now)
    template = render_to_string('ajax_search.html', {'search': all_search})
    return JsonResponse({'data': template})
