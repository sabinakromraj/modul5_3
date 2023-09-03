from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return f"Imię: {self.first_name} Nazwisko: {self.last_name} Telefon: {self.phone_number} Email: {self.email}"

    def contact(self):
        return f"Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return len(self.first_name + " " + self.last_name)
    
class BusinessContact(BaseContact):
    def __init__(self, job, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.business_number = business_number

    def __str__(self):
        base_contact_info = super().__str__()
        return f"{base_contact_info}, Firma: {self.company}, Stanowisko: {self.job}, Telefon służbowy: {self.business_number}"
    
    def contact(self):
        return f"Wybieram numer {self.business_number} i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return len(self.first_name + " " + self.last_name)
    
def create_contacts(contact_type, count):
    fake = Faker()
    contacts = []

    for i in range(count):
        if contact_type == "BaseContact":
            contact = BaseContact(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        elif contact_type == "BusinessContact":
            contact = BusinessContact(fake.job(), fake.company(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.email())
        
        contacts.append(contact)
    
    return contacts

base_contacts = create_contacts("BaseContact", 3)
business_contacts = create_contacts("BusinessContact", 2)

print("Losowe kontakty podstawowe:")
for contact in base_contacts:
    print(contact.contact())

print("\nLosowe kontakty biznesowe:")
for contact in business_contacts:
    print(contact.contact())
