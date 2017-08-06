from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'send_mail$', views.message_to_user, name="send-mail")
]