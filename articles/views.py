from django.shortcuts import render, redirect
from .models import Article     # index
from .forms import ArticleForm  # create
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    articles = Article.objects.all()  # 전체 게시물 조회

    context = {
        'articles':articles,          # context에 전체 게시물 담고
    }

    return render(request, 'index.html', context)

@login_required
def create(request):
    # # 로그인을 안했다면
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login') # 로그인 페이지로 돌아감


    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():                   # title, content는 request.POST에 들어있고 user는 들어있지 않아서 따로 넣어주어야 함
            article = form.save(commit=False) # 잠깐 멈춤
            article.user = request.user       # 로그인한 사람 정보를 입력후 / user 대신 user_id 이렇게 사용해도 됨
            article.save()                    # 저장
            return redirect('articles:index')

    else:
        form = ArticleForm()     # title, comment만 user X

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)