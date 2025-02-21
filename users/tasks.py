import datetime
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def checking_for_active_users():
    """Блокирует если не заходил 30 дней"""
    thirty_days_ago = timezone.now() - datetime.timedelta(days=30)
    users = User.objects.filter(last_login__lt=thirty_days_ago).exclude(
        last_login__isnull=True
    )
    users.update(is_active=False)
    users.save()
