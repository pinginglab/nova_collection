import os

EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.139.com'

EMAIL_PORT = 465

EMAIL_HOST_USER = os.environ.get("EMAIL_SENDER", '19802021029@139.com')  # 帐号

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PWD", '1q1q1q1q1')  # 授权码（****）
# 默认邮件
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
