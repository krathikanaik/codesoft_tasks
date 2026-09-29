class ContactBook:

    def __init__(self):
        # Store contacts in a dictionary where the key is the name
        self.contacts = {}

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return

        if name.lower() in [k.lower() for k in self.contacts.keys()]:
            print("A contact with this name already exists!")
            return

        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()

        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address,
        }
        print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts saved yet.")
            return

        print(f"{'Name':<20} | {'Phone Number':<15}")
        print("-" * 38)
        for name, details in self.contacts.items():
            print(f"{name:<20} | {details['phone']:<15}")

    def search_contact(self):
        print("\n--- Search Contact ---")
        if not self.contacts:
            print("No contacts saved yet.")
            return

        query = input(
            "Enter Name or Phone Number to search: "
        ).strip().lower()
        found = False

        for name, details in self.contacts.items():
            if query in name.lower() or query in details["phone"]:
                print("\nContact Found:")
                print(f"Name   : {name}")
                print(f"Phone  : {details['phone']}")
                print(f"Email  : {details['email']}")
                print(f"Address: {details['address']}")
                found = True

        if not found:
            print("No matching contact found.")

    def update_contact(self):
        print("\n--- Update Contact ---")
        if not self.contacts:
            print("No contacts saved yet.")
            return

        name_to_update = input(
            "Enter the Name of the contact to update: "
        ).strip()

        # Find existing contact key case-insensitively
        target_key = None
        for name in self.contacts:
            if name.lower() == name_to_update.lower():
                target_key = name
                break

        if not target_key:
            print("Contact not found.")
            return

        details = self.contacts[target_key]
        print("\nLeave blank and press Enter to keep the current value.")

        new_phone = input(f"New Phone [{details['phone']}]: ").strip()
        new_email = input(f"New Email [{details['email']}]: ").strip()
        new_address = input(f"New Address [{details['address']}]: ").strip()

        if new_phone:
            details["phone"] = new_phone
        if new_email:
            details["email"] = new_email
        if new_address:
            details["address"] = new_address

        print(f"Contact '{target_key}' updated successfully!")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        if not self.contacts:
            print("No contacts saved yet.")
            return

        name_to_delete = input(
            "Enter the Name of the contact to delete: "
        ).strip()

        target_key = None
        for name in self.contacts:
            if name.lower() == name_to_delete.lower():
                target_key = name
                break

        if target_key:
            del self.contacts[target_key]
            print(f"Contact '{target_key}' deleted successfully!")
        else:
            print("Contact not found.")


def main():
    book = ContactBook()

    while True:
        print("\n" + "=" * 35)
        print("        CONTACT BOOK MENU        ")
        print("=" * 35)
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            book.search_contact()
        elif choice == "4":
            book.update_contact()
        elif choice == "5":
            book.delete_contact()
        elif choice == "6":
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
