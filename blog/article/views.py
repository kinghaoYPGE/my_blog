from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    return HttpResponse(post.title)
