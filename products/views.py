from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user  # 현재 로그인한 유저로 설정
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})
