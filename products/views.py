from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

from django.contrib.auth.decorators import login_required

@login_required
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


def like_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        # 제품이 존재하지 않으면 홈으로 리디렉션
        return redirect('home')

    # 찜하기 기능
    product.liked_by.add(request.user)  # 로그인한 유저를 찜 목록에 추가
    return redirect('product_detail', product_id=product.id)