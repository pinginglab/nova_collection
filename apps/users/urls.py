from django.conf.urls import url

from apps.users.views.CheckUrlView import CheckUrlView

urlpatterns = [
    # # 验证用户注册后，在邮件里点击注册链接
    url(r'active/(?P<active_code>.*)/$', CheckUrlView.as_view, name='active_user'),
    # url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    # url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    # url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),


    # # 用户信息
    # url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    #
    # # 用户头像修改
    # url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    #
    # # 用户个人中心修改密码
    # url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    #
    # # 修改邮箱时 发送邮箱验证码
    # url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    #
    # # 修改邮箱时，验证邮箱和验证码
    # url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    #
    # # 我的课程
    # url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),
    #
    # # 我收藏的课程机构
    # url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),
    #
    # # 我收藏的授课讲师
    # url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    #
    # # 我收藏的课程
    # url(r'^myfav/courses/$', MyFavCourseView.as_view(), name='myfav_course'),
    #
    # # 我的消息
    # url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),
]