from app.models_app.customerModel import Customer


class CustomerDbService:

    @staticmethod
    def get_customers():
        return Customer.objects.all()

    @staticmethod
    def get_by_email(email):
        return Customer.objects.all().filter(email=email).first()

    @staticmethod
    def get_by_id(customer_id):
        return Customer.objects.all().filter(id=customer_id).first()
