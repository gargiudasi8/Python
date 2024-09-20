class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"{self.name}: {self.phone}"
    

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            manager.add_contact(name, phone)
            print(f"Added contact: {name}")

        elif choice == '2':
            print("Contacts:")
            manager.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
            print(f"Deleted contact: {name}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
