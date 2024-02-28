#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

class TelephoneDirectory:
    def __init__(self, file_path='telephone_directory.csv'):
        self.file_path = file_path
        self.contacts = pd.DataFrame(columns=['Name','Number','Place','Mother Name','Father Name'])
        self.load_contacts()

    def load_contacts(self):
        try:
            self.contacts = pd.read_csv(self.file_path)
            print("Telephone directory loaded successfully.")
        except FileNotFoundError:
            print("No existing telephone directory found. Creating a new one.")

    def save_contacts(self):
        self.contacts.to_csv(self.file_path, index=False)
        print("Telephone directory saved successfully.")

    def add_contact(self,name,number,place,mn,fn):
        if name not in self.contacts['Name'].values:
            new_entry = pd.DataFrame([[name, number]], columns=['Name','Number','Place','Mother Name','Father Name'])
            self.contacts = pd.concat([self.contacts, new_entry], ignore_index=True)
            print(f"Contact '{name}' added successfully.")
            self.save_contacts()
        else:
            print(f"Contact '{name}' already exists. Use update_contact to modify.")

    def update_contact(self,name,number,place,mn,fn):
        if name in self.contacts['Name'].values:
            self.contacts.loc[self.contacts['Name'] == name, 'Number'] = new_number
            print(f"Contact '{name}' updated successfully.")
            self.save_contacts()
        else:
            print(f"Contact '{name}' does not exist. Use add_contact to add a new contact.")

    def delete_contact(self, name):
        if name in self.contacts['Name'].values:
            self.contacts = self.contacts[self.contacts['Name'] != name]
            print(f"Contact '{name}' deleted successfully.")
            self.save_contacts()
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        contact = self.contacts[self.contacts['Name'] == name]
        if not contact.empty:
            print(contact)
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        if self.contacts.empty:
            print("No contacts found.")
        else:
            print("Telephone Directory:")
            print(self.contacts)

# Example usage
directory = TelephoneDirectory()

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name to update: ")
        number = input("Enter new number: ")
        place = input("Enter place ")
        mn = input("Mother's Name: ")
        fn = input("Father's Name: ")
        directory.add_contact(name,number,place,mn,fn)
    elif choice == '2':
        name = input("Enter name to update: ")
        number = input("Enter new number: ")
        place = input("Enter place ")
        mn = input("Mother's Name: ")
        fn = input("Father's Name: ")
        directory.update_contact(name,number,place,mn,fn)
    elif choice == '3':
        name = input("Enter name to delete: ")
        directory.delete_contact(name)
    elif choice == '4':
        name = input("Enter name to search: ")
        directory.search_contact(name)
    elif choice == '5':
        directory.display_contacts()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


# In[ ]:




