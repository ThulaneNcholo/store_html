from django.shortcuts import render

# Create your views here.
def IndexView(request):
    return render(request,'client/index.html')


def ViewStore(request):
    return render(request,'client/view_store.html')

def ViewInventory(request):
    return render(request,'client/view_inventory.html')