from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

