from app.dbServices.contactsDbService import ContactsDbService


class ContactsService:
    @staticmethod
    def get_employees():
        return ContactsDbService.get_employees()
