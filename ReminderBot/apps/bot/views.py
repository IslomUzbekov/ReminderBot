
import datetime

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Reminder
from .openai_api import openai_api
from .telegram_bot import send_telegram_message


@csrf_exempt
def handle_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_id = data["message"]["from"]["id"]
        message = data["message"]["text"]

        reminder_time = openai_api.parse_reminder(message)

        # Преобразуйте reminder_time в объект datetime
        remind_at = timezone.now() + datetime.timedelta(hours=reminder_time)

        Reminder.objects.create(user_id=user_id, message=message, remind_at=remind_at)

        send_telegram_message(user_id, f"Напоминание установлено на {remind_at}")
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"}, status=400)
