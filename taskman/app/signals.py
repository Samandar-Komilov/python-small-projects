from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from django_celery_beat.models import PeriodicTask, IntervalSchedule, CrontabSchedule

from app.models import Task
import json


@receiver(post_save, sender=Task)
def schedule_remaining_time(sender, instance, created, **kwargs):
    """Creates a Celery Beat periodic task to send remaining time every 100 seconds."""
    print(">>>> Signal is working!", created)
    if created:
        interval, _ = IntervalSchedule.objects.get_or_create(
            every=100,
            period=IntervalSchedule.SECONDS,
        )

        PeriodicTask.objects.create(
            interval=interval,
            name=f"Send remaining time for {instance.title}",
            task="app.tasks.send_task_reminder",
            args=json.dumps([instance.id]),
        )
        # crontab, _ = CrontabSchedule.objects.get_or_create(
        #     minute="*/1",  # Every 2 minutes (~120 sec, closest we can get)
        #     # second="40",  # Offset by 40 seconds to approximate 100s interval
        # )

        # Create periodic task
        # PeriodicTask.objects.create(
        #     crontab=crontab,
        #     name=f"Send Remaining Time for Task {instance.id}",
        #     task="app.tasks.send_task_reminder",
        #     args=json.dumps([instance.id]),
        # )
