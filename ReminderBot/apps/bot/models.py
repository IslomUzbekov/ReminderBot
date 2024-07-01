from django.contrib.auth.models import User
from django.db import models


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.user.username} at {self.reminder_time}"
