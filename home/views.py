from django.http import HttpResponse
from django.http import JsonResponse


def credits(request):
    content = "Nicky\nJohn"
    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = """<h1>About</h1>
    <p>This is a website for musicians to share their music and connect.</p>"""
    return HttpResponse(content, content_type="text/html")


def version(request):
    content = {"version": "1.0.0"}
    return JsonResponse(content, content_type="text/json")
