from django.views import View
from django.shortcuts import render, redirect
from app.services.productService import ProductService
from app.services.orderService import OrderService
from django import forms
from app.models_app.productModel import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'supplier', 'category', 'price', 'image']


class ProductView(View):
    @staticmethod
    def get(request):
        products = ProductService.get_products()
        popular = ProductService.get_popular()
        if request.GET.get('sort') == 'price' or request.GET.get('sort') == 'name':
            products = Product.objects.all().order_by(request.GET.get('sort'))
            print(products)
            return render(request, 'products.html', {'role': request.session['role'], 'products': products})
        if request.GET.get('search'):
            search_query = request.GET['search']
            products = Product.objects.filter(name__icontains=search_query)
            return render(request, 'products.html',
                          {'role': request.session['role'], 'products': products, 'search_query': search_query})
        return render(request, "products.html",
                      {'role': request.session['role'], 'products': products, 'popular': popular})

    @staticmethod
    def post(request):
        if request.POST.get('action') == 'create':
            return render(request, 'products.html',
                          {'role': request.session['role'],
                           'form': ProductForm(), 'products': ProductService.get_products()})
        form = ProductForm(request.POST, request.FILES)
        try:
            create = ProductService.create(form.data['name'],
                                            int(form.data['supplier']), int(form.data['category']),
                                            int(form.data['price']), form.data['image'])
            if create is not None:
                return redirect('products')
            form.add_error(None, 'Error!')
        except:
            form.add_error(None, 'Error!')
        try:
            product_id = int(request.POST.get('btnBuy'))
            OrderService.create_order(request.session['id'], product_id)
            return render(request, 'products.html',
                          {'role': request.session['role'], 'products': ProductService.get_products()})
        except:
            return render(request, 'products.html',
                          {'role': request.session['role'], 'products': ProductService.get_products()})


class ProductDetailForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'supplier', 'category', 'price']


class ProductDetailView(View):
    @staticmethod
    def get(request, product_id):
        product = ProductService.get_product_by_id(product_id)
        return render(request, 'product-details.html',
                      {'role': request.session['role'], 'product': product})

    @staticmethod
    def post(request, product_id):
        if request.session['role'] != 'admin':
            return redirect('products')
        if request.POST.get('action') == 'edit':
            product = ProductService.get_product_by_id(product_id)
            form = ProductDetailForm(initial={'name': product.name, 'supplier': product.supplier,
                                              'category': product.category, 'price': product.price})
            return render(request, 'product-details.html',
                          {'role': request.session['role'], 'form': form,
                           'product': product, 'action': request.POST.get('action')})
        if request.POST.get('action') == 'delete':
            ProductService.delete(product_id)
            return redirect('products')

        form = ProductDetailForm(request.POST)
        if form.is_valid():
            try:
                update = ProductService.update(form.data['name'],
                                               int(form.data['supplier']), int(form.data['category']),
                                               int(form.data['price']), form.data['image'], product_id)
                if update is None:
                    form.add_error(None, 'Some error')
                else:
                    form = None
                    return redirect('products')
            except:
                form.add_error(None, 'Some unexpected error')
        return render(request, 'product-details.html',
                      {'role': request.session['role'], 'product': ProductService.get_product_by_id(product_id),
                       'form': form, 'action': request.POST.get('action')})
