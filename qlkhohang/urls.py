# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('suahanghoa/', views.sushanghoa, name='them_hanghoa'),  # Thêm mới
    path('suahanghoa/<int:id_hanghoa>/', views.sushanghoa, name='sua_hanghoa'),  # Chỉnh sửa
    path('dshanghoa/', views.danh_sach_hanghoa, name='dshanghoa'),  # Giả sử bạn có trang này
]
