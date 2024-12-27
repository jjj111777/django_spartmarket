"""
URL configuration for spartmarket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# spartmarket/urls.py
from django.contrib import admin
from django.urls import path
from accounts import views as accounts_views
from products import views as products_views  # 'products' 앱에서 views를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),  # 홈 페이지 경로 추가
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name='logout'),
    path('profile/', accounts_views.profile, name='profile'),
    path('product/<int:product_id>/like/', products_views.like_product, name='like_product'),  # 'products' 앱에서 like_product 뷰 가져오기
]
