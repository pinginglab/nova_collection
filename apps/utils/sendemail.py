
from random import Random

from django.core.mail import send_mail
from django.http import HttpResponse

from apps.users.models import EmailVerifyRecord
from nova_collection.conf.email import DEFAULT_FROM_EMAIL


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGg1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # 保存到数据库完成


def send_my_email(req, reciever):
    title = "美团骑手offer"
    msg = "恭喜你成为美团骑手"
    email_from = DEFAULT_FROM_EMAIL
    # 发送邮件
    send_mail(title, msg, email_from, reciever)
    return HttpResponse("ok")
