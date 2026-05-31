from django.shortcuts import HttpResponse,redirect
from django.http import HttpResponseNotFound, JsonResponse


def hello_view(request):
    return HttpResponse("Hello World сыллка на страницу <a href='http://127.0.0.1:8000/hello/aboutus/'> О нас</a>")
def hello_view2(request):
    return HttpResponse("О нас ссылка на <a href='http://127.0.0.1:8000/hello/'>Главную страницу</a>")
def hello_numbers(request,text):
    return HttpResponse(f"Это специальная страница для Url с цифрами или буквами отправленный текст:{text}")
def hello_id(request,id):
    return HttpResponse(f"Это страница с id и вот оно:{id}")
def hello_info(request):
    method = request.method
    path = request.path
    user_agent = request.headers.get("User-Agent")
    host = request.get_host()
    response = f"Метод {method}, путь {path},и все остально {user_agent},{host}"
    return HttpResponse(response)
def hello_user(request,username):
    response = HttpResponse(f"Имя:{username}")
    response["Secret-Code"] = "12344321"
    return response
def hello_blogs(request):
    article_id = request.GET.get("id")
    if article_id:
        if article_id.isdigit() and int(article_id) == 1:
            return HttpResponse(f"блог")
        else:
            return HttpResponse("Ошибка: ID должен быть числом", status=400)
    return HttpResponse("1-блоги news - новости")
def hello_news(request, name):
    if name == "news":
        return HttpResponse("Новость дня 30 надо в школу")
    else:
        return HttpResponseNotFound("Page not found")

def hello_address(request,name):
    if name == "contact-us":
        return redirect("/hello/aboutus/")
def hello_json(request):
    return JsonResponse({"hello":"world"})
def set_cookies(request):
    response = HttpResponse("Cookies set")
    response.set_cookie("username","admin",max_age=3600)
    return response
def get_cookies(request):
    username = request.COOKIES.get("username")
    if (username):
        return JsonResponse({"username":username})
    else:
        return HttpResponseNotFound("At first you need download cookies")
