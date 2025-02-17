from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.utils.timezone import now

from app.models import Task


@shared_task
def send_task_reminder(task_id):
    """Sends the remaining time via WebSocket every 100 seconds."""
    try:
        task = Task.objects.get(id=task_id)
        remaining_time = int((task.due_date - now).total_seconds())

        if remaining_time <= 0:
            return f"Task with ID {task_id} has already expired"
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {"type": "send_notification", "message": f"Reminder for task: {task.title} is due soon! Time remaining: {remaining_time} seconds"},
        )
        return f"Reminder sent for task: {task.title}"
    except Task.DoesNotExist:
        return f"Task with ID {task_id} does not exist"