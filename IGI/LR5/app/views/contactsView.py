from django.views import View
from django.shortcuts import render
from app.services.contactsService import ContactsService


class ContactsView(View):
    @staticmethod
    def get(request):
        employees = ContactsService.get_employees()
        return render(request, 'contacts.html',
                      {'role': request.session['role'], 'employees': employees})
