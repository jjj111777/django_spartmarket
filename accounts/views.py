from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

#회원가입
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '회원가입이 완료되었습니다!')
            return redirect('login')  # 로그인 페이지로 리디렉션
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

#로그인
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 로그인 후 홈으로 이동
        else:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
    return render(request, 'accounts/login.html')

#로그아웃
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('home')  # 로그아웃 후 홈으로 이동

#유저 프로필
def profile(request):
    user = request.user
    # 유저가 등록한 물건과 찜한 물건을 가져옵니다.
    user_products = user.products.all()
    liked_products = user.liked_products.all()

    return render(request, 'accounts/profile.html', {
        'user': user,
        'user_products': user_products,
        'liked_products': liked_products
    })

#홈 페이지 설정정
def home(request):
    return render(request, 'home.html')  # 'home.html' 템플릿을 렌더링