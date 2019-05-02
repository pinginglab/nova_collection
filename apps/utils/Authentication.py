import jwt
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse

from apps.users.models import PingUser
from nova_collection import settings


def auth_permission_required(perm):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # 格式化权限
            perms = (perm,) if isinstance(perm, str) else perm

            if request.user.is_authenticated:
                # 正常登录用户判断是否有权限
                if not request.user.has_perms(perms):
                    raise PermissionDenied
            else:
                try:
                    auth = request.META.get('HTTP_AUTHORIZATION').split()
                except AttributeError:
                    return JsonResponse({"code": 401, "message": "No authenticate header"})

                # 用户通过API获取数据验证流程
                if auth[0].lower() == 'token':
                    try:
                        # dict = self.get_message(auth[1], self.Signature, self.algorithm)
                        dict = jwt.decode(auth[1], settings.SECRET_KEY, algorithms=['HS256'])
                        username = dict.get('data').get('username')
                    except jwt.ExpiredSignatureError:
                        return JsonResponse({"status_code": 401, "message": "Token expired"})
                    except jwt.InvalidTokenError:
                        return JsonResponse({"status_code": 401, "message": "Invalid token"})
                    except Exception as e:
                        return JsonResponse({"status_code": 401, "message": "Can not get user object"})

                    try:
                        user = PingUser.objects.get(username=username)
                    except PingUser.DoesNotExist:
                        return JsonResponse({"status_code": 401, "message": "User Does not exist"})

                    if not user.is_active:
                        return JsonResponse({"status_code": 401, "message": "User inactive or deleted"})

                    # Token登录的用户判断是否有权限
                    if not user.has_perms(perms):
                        return JsonResponse({"status_code": 403, "message": "PermissionDenied"})
                else:
                    return JsonResponse({"status_code": 401, "message": "Not support auth type"})

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


class Authentication(object):
    def __init__(self, Payload, algorithm='HS256'):
        self.Payload = Payload
        self.Signature = settings.SECRET_KEY
        self.algorithm = algorithm
        self.UserModel = get_user_model()

    def set_token(self):
        encoded_jwt = jwt.encode(self.Payload, self.Signature, self.algorithm)
        return encoded_jwt

    def get_message(self, token, Signature, algorithm='HS256'):
        decoded_jwt = jwt.decode(token, Signature, algorithm)
        return decoded_jwt

