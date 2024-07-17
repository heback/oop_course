from typing import List


class Contact:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class ContactList:
    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def search(self, name: str) -> List[Contact]:
        return [contact for contact in self.contacts if name in contact.name]

# 예제 사용
contact_list = ContactList()
contact_list.add_contact(Contact("Alice", "alice@example.com"))
contact_list.add_contact(Contact("Bob", "bob@example.com"))

result = contact_list.search("Alice")
for contact in result:
    print(contact.name, contact.email)