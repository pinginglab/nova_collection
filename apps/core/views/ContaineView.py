import os
import random
import socket

import docker
from django.http import JsonResponse
from rest_framework.views import APIView

from apps.utils.Authentication import set_token


def IsOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        # s.shutdown(2)
        # 利用shutdown()函数使socket双向数据传输变为单向数据传输。shutdown()需要一个单独的参数，
        # 该参数表示了如何关闭socket。具体为：0表示禁止将来读；1表示禁止将来写；2表示禁止将来读和写。
        return 1
    except:
        return 0


class ContainerView(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def __init__(self):
        self.client = docker.from_env()

    def get(self, request):
        # data = request.body.decode('utf-8')
        # data = json.loads(data)
        """
            create container for images
        """
        ip = '0.0.0.0'
        while True:
            port = random.randint(10000, 30000)
            if not IsOpen(ip, port.__str__()):
                self.client.containers.run("webgoat/webgoat-7.1", detach=True, ports={'8080/tcp': port})
                url = '{}:{}/WebGoat/login.mvc'.format(os.environ.get('IP', '127.0.0.1'), port)
                # url = set_token(url)
                return JsonResponse({"url": url})
            else:
                continue
