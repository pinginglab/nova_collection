from celery import task
from django.core.mail import send_mail

from nova_collection import settings


@task
def send_email(email):
    title = '邮件的标题'
    msg = '异步操作'
    from_email = settings.DEFAULT_FROM_EMAIL
    recievers = [email, ]
    send_mail(
        title,
        msg,
        from_email,
        recievers,
        # 发送异常时不提示
        fail_silently=True
    )
