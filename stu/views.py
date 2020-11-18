from django.shortcuts import render,HttpResponse
import json
# 打开登录页面.
def login(request):
    return render(request,"login.html")

# 判断用户名和密码是否正确
def islogin(request):
    # 初始化返回的数据(json数据格式，类似于字典)
    result = {"code":-1,"msg":"用户名不存在"}
    # 获取提交过来的用户名和密码
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 开始判断
    if username == "201801":# 判断用户名
        # 判断密码
        if password == "123":
            # 密码正确
            result["code"] = 0
            result["msg"] = "密码正确"
        else:
            # 密码不正确
            result["code"] = -2
            result["msg"] = "密码不正确"
    return HttpResponse(json.dumps(result))

# 打开主页面
def index(request):
    return render(request,"index.html")