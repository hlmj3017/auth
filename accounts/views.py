from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login  # 이름 중복으로 오류 발생할 수 있으므로
from django.contrib.auth import logout as auth_logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')

    else:
        # user가 id와 password를 입력받는 빈 폼 
        form = CustomUserCreationForm()
        

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST) # 기존 정보를 request에 덮어씀

        if form.is_valid():
            # form인증이 되었다면, 
            # form의 get_user를 넣어주는 함수를 불러온다.
            auth_login(request, form.get_user()) # get_user: authentication에만 있는 기능 / 아이디를 찾아서 form에 불러오는 것
            # get_user 해당하는 아이디를 찾아서
            # form에 불러와 
            # 요청값에 씌움
            # login으로 하겠다. 
            return redirect('accounts:login')


    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')