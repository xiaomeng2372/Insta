#manage app's urls

from django.contrib import admin
from django.urls import path
from Insta.views import HelloWorld
# 调用asview 函数
urlpatterns = [
  path('', HelloWorld.as_view(), name='helloworld') 
 ]
