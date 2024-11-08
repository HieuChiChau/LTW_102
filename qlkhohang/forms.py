from django import forms
from .models import HangHoa

class HangHoaForm(forms.ModelForm):
    class Meta:
        model = HangHoa
        fields = ['ten', 'mota', 'don_vi_tinh']  # Các trường cần có trong form
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập tên'
            }),
            'mota': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Nhập mô tả'
            }),

            'don_vi_tinh': forms.Select(attrs={
                'class': 'form-control'
            }),
        }