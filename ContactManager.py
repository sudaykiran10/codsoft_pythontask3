import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = {}  

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required!")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join(f"{name}: {contact['phone']}" for name, contact in self.contacts.items())
            messagebox.showinfo("Contacts", f"Contact List:\n\n{contact_list}")
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        else:
            messagebox.showinfo("Contact Details", f"No contact found with the name '{name}'.")

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email
            self.contacts[name]['address'] = address

            messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with the name '{name}'.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", f"No contact found with the name '{name}'.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
