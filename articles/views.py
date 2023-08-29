from django.shortcuts import render
from .models import Article

# Create your views here.


def index(request):

    articles = Article.objects.all()  # 전체 게시물 조회

    context = {
        'articles':articles,          # context에 전체 게시물 담고
    }

    return render(request, 'index.html', context)
