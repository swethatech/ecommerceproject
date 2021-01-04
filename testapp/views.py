from django.shortcuts import render, redirect
from testapp.models import Ecommerce
from django.views.generic import DetailView
from testapp.forms import ConfirmationForm


def fetch_products(request):
    ecommerce = Ecommerce.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        ecommerce = ecommerce.filter(name__contains=item_name)
    my_dict = {'ecommerce': ecommerce}
    return render(request, "home.html", my_dict)


class EcommerceDetailView(DetailView):
    model = Ecommerce

def confirm_view(request):
    form = ConfirmationForm()
    if request.method=='POST':
        form = ConfirmationForm(request.POST)
        if form.is_valid():
          form.save(commit=True)
        return redirect('/success')
    my_dict = {'form': form}
    return render(request, "order.html", my_dict)


def end(request):
    return render(request, "success.html")





