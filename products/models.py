from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 찜하기 기능 추가
    liked_by = models.ManyToManyField(User, related_name='liked_products', blank=True)

    def __str__(self):
        return self.name
