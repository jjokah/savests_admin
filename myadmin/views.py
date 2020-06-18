from datetime import timedelta

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone

from .forms import EmailPostForm


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


def users_list(request):
    users = User.objects.all()
    return render(request,
                  'myadmin/users.html',
                  {'section': 'users',
                   'users': users})


def email_users(request):
    sent = False
    users_email = list(User.objects.values_list('email', flat=True))

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            sender = request.user.email
            subject = "Message from Admin"
            message = cd['message']
            send_mail(subject, message, sender, users_email)
            sent = True
    else:
        form = EmailPostForm()

    return render(request,
                  'myadmin/email_users.html',
                  {'section': 'email',
                   'form': form,
                   'sent': sent,
                   })
