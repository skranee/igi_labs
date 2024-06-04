# Lab 4: Product Manager
# Version 1.0
# Developer: Abmetko Pavel
# Date: 04.13.2024

import csv
import pickle


class Product:
    """
    Represents a product with its attributes.
    """

    def __init__(self, name, country, importer, quantity, exported):
        """
        Initialize a product with name, country, importer, quantity and exported countries.

        Args:
            name (str): The name of the product.
            country (str): The country exporting the product.
            importer (str): The importing country.
            quantity (int): The quantity of the product being exported.
            exported (str): The countries product is exported at.
        """
        self.name = name
        self.country = country
        self.importer = importer
        self.quantity = quantity
        self.exported = exported


class ProductManager:
    """
    Manages products including adding, searching, and exporting.
    """

    def __init__(self):
        """
        Initialize the ProductManager with an empty list of products.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the product manager.

        Args:
            product (Product): The product to be added.
        """
        self.products.append(product)

    def search_product_by_name(self, name):
        """
        Search for a product by its name.

        Args:
            name (str): The name of the product to search for.

        Returns:
            Product or None: The product found with the given name or None if not found.
        """
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None

    def get_export_countries(self, product_name):
        """
        Get the list of countries to which the given product is exported.

        Args:
            product_name (str): The name of the product.

        Returns:
            list: A list of countries to which the product is exported.
        """
        export_countries = []
        total_quantity = 0
        for product in self.products:
            if product.name.lower() == product_name.lower():
                export_countries.append(product.exported)
                total_quantity += product.quantity
        return export_countries, total_quantity

    def export_to_csv(self, filename):
        """
        Export the products to a CSV file.

        Args:
            filename (str): The name of the CSV file to export to.
        """
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Country', 'Importer', 'Quantity', 'Exported']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product in self.products:
                writer.writerow({'Name': product.name, 'Country': product.country, 'Importer': product.importer, 'Quantity': product.quantity, 'Exported': product.exported})

    def export_to_pickle(self, filename):
        """
        Export the products to a pickle file.

        Args:
            filename (str): The name of the pickle file to export to.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self.products, file)

    @classmethod
    def import_from_csv(cls, filename):
        """
        Import products from a CSV file.

        Args:
            filename (str): The name of the CSV file to import from.

        Returns:
            ProductManager: A ProductManager instance containing imported products.
        """
        product_manager = cls()
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Product(row['Name'], row['Country'], row['Importer'], int(row['Quantity']), row['Exported'])
                product_manager.add_product(product)
        return product_manager

    @classmethod
    def import_from_pickle(cls, filename):
        """
        Import products from a pickle file.

        Args:
            filename (str): The name of the pickle file to import from.

        Returns:
            ProductManager: A ProductManager instance containing imported products.
        """
        with open(filename, 'rb') as file:
            products = pickle.load(file)
            product_manager = cls()
            product_manager.products = products
        return product_manager


def main():
    """
    Main function to demonstrate product management.
    """
    print("Welcome to Product Manager")

    manager = ProductManager()

    while True:
        # Adding products
        manager.add_product(Product("IPhone", "USA", "France", 100, "Italy, Britain, Belarus, Zimbabwe"))
        manager.add_product(Product("MacBook", "Canada", "Germany", 200, "Kazakhstan, Australia, Hungary"))
        manager.add_product(Product("AirPods Pro", "USA", "Belgium", 300, "Lithuania, Latvia, Poland"))

        # Exporting to CSV and pickle
        manager.export_to_csv("products.csv")
        manager.export_to_pickle("products.pkl")

        # Importing from CSV and pickle
        imported_manager_csv = ProductManager.import_from_csv("products.csv")
        imported_manager_pickle = ProductManager.import_from_pickle("products.pkl")

        # Searching product by name
        search_name = input("Enter product name to get export details: ")
        export_countries, total_quantity = imported_manager_csv.get_export_countries(search_name)
        if export_countries:
            print(f"Product: {search_name}")
            print("Export Countries:", export_countries)
            print("Total Export Volume:", total_quantity)
        else:
            print("Product not found")

        choice = input("\nDo you want to run the program again? (yes/no): ").lower()
        if choice != "yes":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
