
from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from .models import Reminder
from .telegram_bot import send_telegram_message


@shared_task
def check_reminders():
    now = timezone.now()
    reminders = Reminder.objects.filter(remind_at__lte=now)
    for reminder in reminders:
        send_telegram_message(reminder.user_id, reminder.message)
        reminder.delete()
