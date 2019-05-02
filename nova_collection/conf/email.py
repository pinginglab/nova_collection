import os

EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.qq.com'

EMAIL_PORT = 465

EMAIL_HOST_USER = os.environ.get("EMAIL_SENDER", 'treestore@foxmail.com')  # 帐号

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PWD", 'en4478593')  # 授权码（****）
# 默认邮件
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
