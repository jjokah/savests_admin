from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def dashboard(request):
    now = timezone.now()
    a_day_ago = now - timedelta(hours=24)
    a_week_ago = now - timedelta(days=7)
    a_month_ago = now - timedelta(days=30)

    created_within_a_day = User.objects.filter(
        date_joined__range=(a_day_ago, now)).count()
    created_within_a_week = User.objects.filter(
        date_joined__range=(a_week_ago, now)).count()
    created_within_a_month = User.objects.filter(
        date_joined__range=(a_month_ago, now)).count()

    return render(request,
                  'myadmin/dashboard.html',
                  {'section': 'dashboard',
                   'created_within_a_day': created_within_a_day,
                   'created_within_a_week': created_within_a_week,
                   'created_within_a_month': created_within_a_month})
