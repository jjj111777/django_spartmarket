from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    # 찜하기 모델 추가
    class Product(models.Model):
    # 기존 필드들...
    liked_by = models.ManyToManyField(User, related_name='liked_products', blank=True)


# 찜하기 뷰 추가
def like_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.liked_by.add(request.user)  # 로그인한 유저를 찜 목록에 추가
    return redirect('product_detail', product_id=product.id)

