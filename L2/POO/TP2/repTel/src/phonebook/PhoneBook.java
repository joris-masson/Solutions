package phonebook;

import java.util.ArrayList;
import java.util.Objects;

public class PhoneBook {
    ArrayList<Contact> contactList;

    public PhoneBook() {
        this.contactList = new ArrayList<Contact>();
    }

    public void addContact(String name, String phoneNumber) {
        Contact zeNewContact = new Contact(name, phoneNumber);
        this.contactList.add(zeNewContact);
    }

    public ArrayList<String> getPhoneNumbers(String name) {
        ArrayList<String> correspond = new ArrayList<String>();

        for (int i = 0; i < this.contactList.size(); i++) {
            if (this.contactList.get(i).getName() == name) {
                correspond.add(this.contactList.get(i).getPhoneNumber());
            }
        }
        return correspond;
    }

    public ArrayList<String> getNames(String phoneNumber) {
        ArrayList<String> correspond = new ArrayList<String>();

        for (Contact contact : this.contactList) {
            if (Objects.equals(contact.getPhoneNumber(), phoneNumber)) {
                correspond.add(contact.getName());
            }
        }
        return correspond;
    }

}
