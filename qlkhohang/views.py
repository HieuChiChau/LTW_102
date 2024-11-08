from django.shortcuts import render, get_object_or_404, redirect
from .forms import HangHoaForm
from .models import *
from django.contrib import messages

def sushanghoa(request, id_hanghoa=None):
    if id_hanghoa:
        # Update
        hanghoa = get_object_or_404(HangHoa, id=id_hanghoa)
        form = HangHoaForm(request.POST or None, instance=hanghoa)
        action = "SỬA THÔNG TIN MẶT HÀNG"
        success_message = f"Các thông tin điều chỉnh của mặt hàng {hanghoa.ten} đã được lưu lại"
    else:
        # Add
        form = HangHoaForm(request.POST or None)
        action = "THÊM MỚI MẶT HÀNG"
        success_message = None

    if form.is_valid():
        form.save()
        if success_message:
            messages.success(request, success_message)
        else:
            messages.success(request, f"Thêm mặt hàng {form.cleaned_data['ten']} thành công")
        return redirect('dshanghoa')
    
    return render(request, 'suahanghoa.html', {
        'form': form,
        'action': action,
        'success_message': success_message
    })

def danh_sach_hanghoa(request):
    hanghoa_list = HangHoa.objects.all()
    return render(request, 'dshanghoa.html', {'hanghoa_list': hanghoa_list})