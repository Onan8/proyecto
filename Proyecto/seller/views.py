from django.shortcuts import render, get_object_or_404, redirect
from .models import Seller
from .forms import SellerForm

#modelo CURD
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller/seller_list.html', {'sellers': sellers})

def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    return render(request, 'seller/seller_detail.html', {'seller': seller})


def seller_create(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm()
    return render(request, 'seller/seller_form.html', {'form': form})

def seller_update(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SellerForm(instance=seller)
    return render(request, 'seller/seller_form.html', {'form': form})

def seller_delete(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == 'POST':
        seller.delete()
        return redirect('seller_list')
    return render(request, 'seller/seller_confirm_delete.html', {'seller': seller})

