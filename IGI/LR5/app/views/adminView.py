from django.views import View
from django.shortcuts import render, redirect
from app.services.adminService import AdminService
from app.dbServices.customerDbService import CustomerDbService
from app.models_app.supplierModel import Supplier


class AdminView(View):
    @staticmethod
    def get(request):
        if request.session['role'] == '' or request.session['role'] == 'user':
            return redirect('home')
        stat = AdminService.draw_customers_stat()
        customers = CustomerDbService.get_customers()
        suppliers = Supplier.objects.all()
        return render(request, 'admin.html',
                      {'role': request.session['role'], 'customers': customers, 'suppliers': suppliers})
