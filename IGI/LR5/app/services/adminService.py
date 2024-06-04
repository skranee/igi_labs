from app.services import productService
from app.dbServices.customerDbService import CustomerDbService
from datetime import datetime
from collections import Counter
from matplotlib import pyplot as plt
from numpy import polyfit, array


class AdminService:

    @staticmethod
    def draw_customers_stat():
        customers = CustomerDbService.get_customers()

        customer_names = [customer.name.split(' ')[0] for customer in customers]

        name_counts = Counter(customer_names)

        names = list(name_counts.keys())
        counts = list(name_counts.values())

        plt.figure(figsize=(10, 6))
        plt.bar(names, counts)
        plt.xlabel('Name')
        plt.ylabel('Quantity')
        plt.title('Name separation')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('./app/static/stats/customerNames.jpg')
        plt.clf()
