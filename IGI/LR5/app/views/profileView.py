from django.views import View
from django.shortcuts import render
from app.dbServices.customerDbService import CustomerDbService
from datetime import datetime, timezone
from calendar import month
from app.dbServices.employee_db_service import EmployeeDbService


class ProfileView(View):
    @staticmethod
    def get(request):
        role = request.session['role']
        if role is 'user':
            user = CustomerDbService.get_by_id(request.session['id'])
        elif role is not '':
            user = EmployeeDbService.get_by_id(request.session['id'])
        else:
            user = None
        date_utc = datetime.now(timezone.utc)
        date = date_utc.astimezone()
        time_zone = f'{str(date.tzinfo).split(" ")[0]} / GMT: {str(date.utcoffset())}'
        return render(request, 'profile.html',
                      {'role': request.session['role'],
                       'user': user,
                       'date_utc': date_utc.strftime('%d/%m/%Y %H:%M'),
                       'date': date.strftime('%d/%m/%Y %H:%M'),
                       'timezone': time_zone,
                       'calendar': month(date.year, date.month)})
