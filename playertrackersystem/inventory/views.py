# item_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import inventory
from .forms import inventoryForms

def item_list(request):
    items = inventory.objects.all()  # This should return all items
    return render(request, 'inventory/item_list.html', {'items': items})


def item_create(request):
    if request.method == "POST":
        form = inventoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = inventoryForms()
    return render(request, 'inventory/item_form.html', {'form': form})

def item_detail(request, pk):
    item = get_object_or_404(inventory, pk=pk)
    return render(request, 'inventory/item_detail.html', {'item': item})

def item_update(request, pk):
    item = get_object_or_404(inventory, pk=pk)
    if request.method == 'POST':
        form = inventoryForms(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = inventoryForms(instance=item)
    return render(request, 'inventory/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(inventory, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'inventory/item_confirm_delete.html', {'item': item})
