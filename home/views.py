from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


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


def news(request):
    data = {
        "news": [
            "RiffMates now has a news pages!",
            "RiffMates now has a web page!",
        ]
    }

    return render(request, "news2.html", data)
