from django.db import models

# Create your models here.

class Kho(models.Model):
    ten = models.CharField(max_length=100, null=False)
    dia_chi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ten

class HangHoa(models.Model):
    ten = models.CharField(max_length=200, null=False)
    mota = models.TextField(blank=True, null=True)

    class DonViTinh(models.TextChoices):
        KG = 'Kg', 'Kg'
        CAI = 'Cái', 'Cái'
        CHAI = 'Chai', 'Chai'
        HOP = 'Hộp', 'Hộp'
    
    don_vi_tinh = models.CharField(max_length=4, choices=DonViTinh.choices, null=False)
    kho = models.ManyToManyField(Kho, through='KhoHangHoa', related_name='hanghoa')

    def __str__(self):
        return self.ten

class KhoHangHoa(models.Model):
    hanghoa = models.ForeignKey(HangHoa, on_delete=models.CASCADE)
    kho = models.ForeignKey(Kho, on_delete=models.CASCADE)
    so_luong = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.hanghoa.ten} - {self.kho.ten} (SL: {self.so_luong})"