from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm

def home(request):
    return equipment_list(request)

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'inventory/equipment_list.html', {'equipments': equipments})

def add_equipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'inventory/add_equipment.html', {'form': form})

def delete_equipment(request):
    equipments = Equipment.objects.all()
    if request.method == "POST":
        equipment_id = request.POST.get('equipment_id')
        equipment = Equipment.objects.get(id=equipment_id)
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'inventory/delete_equipment.html', {'equipments': equipments})
