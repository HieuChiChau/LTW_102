from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import HangHoa, Kho, KhoHangHoa

admin.site.site_header = "QUẢN LÝ KHO"
admin.site.site_title = "QUẢN LÝ KHO"
admin.site.index_title = "Chào mừng đến với hệ thống Quản lý Kho"

@admin.register(HangHoa)
class HangHoaAdmin(admin.ModelAdmin):
    list_display = ('ten', 'mota', 'don_vi_tinh')
    search_fields = ('ten', 'mota')
    list_filter = ('don_vi_tinh',)

@admin.register(Kho)
class KhoAdmin(admin.ModelAdmin):
    list_display = ('ten', 'dia_chi') 
    search_fields = ('ten', 'dia_chi') 

@admin.register(KhoHangHoa)
class KhoHangHoaAdmin(admin.ModelAdmin):
    list_display = ('hanghoa__ten', 'kho__ten', 'so_luong')
    list_filter = ('kho',)
    search_fields = ('hanghoa__ten', 'kho__ten') 
