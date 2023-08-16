class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added successfully.")

    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Number: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        print("Contacts in the phone book:")
        for name, number in self.contacts.items():
            print(f"Name: {name}, Number: {number}")

def main():
    phone_book = PhoneBook()

    while True:
        print("\nPhone Book Management System")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. List Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            phone_book.add_contact(name, number)
        elif choice == "2":
            name = input("Enter name: ")
            new_number = input("Enter new number: ")
            phone_book.update_contact(name, new_number)
        elif choice == "3":
            name = input("Enter name: ")
            phone_book.delete_contact(name)
        elif choice == "4":
            name = input("Enter name: ")
            phone_book.search_contact(name)
        elif choice == "5":
            phone_book.list_contacts()
        elif choice == "6":
            print("Exiting Phone Book Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
