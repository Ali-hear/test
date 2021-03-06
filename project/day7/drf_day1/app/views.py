from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.response import Response
from rest_framework.views import APIView

# @csrf_protect 为某个视图单独添加csrf认证
from app.models import User


@csrf_exempt  # 为某个视图免除csrf认证
def user(request):
    if request.method == "GET":
        username = request.GET.get("username")
        print(username)
        print("GET 查询")
        return HttpResponse("GET OK")
    if request.method == "POST":
        print("POST 新增")
        return HttpResponse("POST OK")
    if request.method == "PUT":
        print("PUT 修改")
        return HttpResponse("PUT OK")
    if request.method == "DELETE":
        print("DELETE 删除")
        return HttpResponse("DELETE OK")


"""
函数视图: function view  基于函数定义的视图
类视图:    class view    基于类定义的视图
"""

"""
单个: 查询单个  查询所有  新增单个  删除单个  修改单个  局部修改单个
群体: 新增多个  删除单个  修改多个  局部修改多个
"""


@method_decorator(csrf_exempt, name="dispatch")  # 为类视图免除csrf认证
class UserView(View):

    def get(self, request, *args, **kwargs):
        """
        提供查询单个用户以及  多个用户的接口
        :param request:  请求对象
        :param args:
        :param kwargs:
        :return: 返回查询结果
        """
        user_id = kwargs.get("id")

        if user_id:

            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            print(user)
            if user:
                # 如果查询出用户的信息, 则返回到前端
                return JsonResponse({
                    "status": 200,
                    "message": "查询单个用户成功",
                    "results": user_val
                })
        else:
            # 用户id不存在 则代表查询所有用户信息
            user_objects_all = User.objects.all().values("username", "password", "gender")
            if user_objects_all:
                return JsonResponse({
                    "status": 200,
                    "message:": "查询所有用户成功",
                    "results": list(user_objects_all)
                })

        return JsonResponse({
            "status": 400,
            "message": "查询用户失败",
        })

    def post(self, request, *args, **kwargs):
        """
        新增单个用户
        """

        username = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 200,
                "message": "新增单个用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })

        except:
            return JsonResponse({
                "status": 400,
                "message": "新增失败",
            })

    def put(self, request, *args, **kwargs):
        print("put 修改")
        return HttpResponse("put OK")

    def delete(self, request, *args, **kwargs):
        print("delete 删除")
        return HttpResponse("delete OK")


class StudentAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print("DRF GET VIEW")
        return Response("DRF GET OK")

    def post(self, request, *args, **kwargs):
        print("POST GET VIEW")
        return Response("DRF POST OK")
