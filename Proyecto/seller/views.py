from django.shortcuts import render, redirect, get_object_or_404
from .models import Seller
from .forms import SellerForm

# Create your views here.

# Crear un nuevo Seller
def seller_create(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller_list')
    else:
        form = SellerForm()
    return render(request, 'seller/seller_form.html', {'form': form})

# Listar todos los Sellers
def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller/seller_list.html', {'sellers': sellers})

# Detallar un Seller específico
def seller_detail(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    return render(request, 'seller/seller_detail.html', {'seller': seller})

# Editar un Seller existente
def seller_update(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == "POST":
        form = SellerForm(request.POST, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('seller_detail', pk=seller.pk)
    else:
        form = SellerForm(instance=seller)
    return render(request, 'seller/seller_form.html', {'form': form})

# Eliminar un Seller
def seller_delete(request, pk):
    seller = get_object_or_404(Seller, pk=pk)
    if request.method == "POST":
        seller.delete()
        return redirect('seller_list')
    return render(request, 'seller/seller_confirm_delete.html', {'seller': seller})
