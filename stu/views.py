from django.shortcuts import render

# 打开登录页面.
def login(request):
    return render(request,"login.html")
