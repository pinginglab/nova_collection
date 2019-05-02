from django.conf.urls import url

from apps.core.views.ContaineView import ContainerView
from apps.core.views.TestView import TestView

urlpatterns = [
    # url(r'^heyluckydog/heyluckydog/heyluckydog/$', TestView.as_view(), name='lucygay'),
    url(r'^container/', ContainerView.as_view(), name='ex'),
]
