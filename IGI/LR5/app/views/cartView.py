from django.views import View
from django.shortcuts import render, redirect
from app.services.orderService import OrderService
from django import forms
from app.dbServices.promoDBService import PromoDbService
from app.services.salesService import SalesService


class CartForm(forms.Form):
    address = forms.CharField(max_length=100, required=True, initial='Minsk, ')
    promo = forms.CharField(max_length=20, required=False)

    def clean_address(self):
        if len(self.cleaned_data['address'].strip()) == 0:
            self.add_error(None, 'Enter a valid address')
            return 0
        return self.cleaned_data['address']

    def clean_promo(self):
        if PromoDbService.check_existence(self.cleaned_data['promo']) is None:
            self.add_error(None, 'Not existing promo code')
            return 0
        return self.cleaned_data['promo']


class CartView(View):
    @staticmethod
    def get(request):
        orders = OrderService.get_orders_by_id(request.session['id'])
        price = 0
        for order in orders:
            price += order.product.price
        return render(request, "cart.html",
                      {'role': request.session['role'], 'orders': orders, 'price': price})

    @staticmethod
    def post(request):
        form = CartForm(request.POST)
        price = 0
        orders = OrderService.get_orders_by_id(request.session['id'])
        products = []
        for order in orders:
            price += order.product.price
            products.append(order.product)
        if form.is_valid():
            try:
                check_promo = PromoDbService.check_existence(form.cleaned_data['promo'])
                if check_promo is True:
                    discount = PromoDbService.get_discount(form.cleaned_data['promo'])
                else:
                    discount = 0
                price = int(price * (1 - float(discount / 100)))
                SalesService.create_sale(products, price, form.cleaned_data['address'], request.session['id'])
                OrderService.delete_orders(orders)
                return redirect('products')
            except:
                form.add_error(None, 'Some unpredicted error')
        return render(request, 'cart.html',
                      {'role': request.session['role'], 'form': form})
