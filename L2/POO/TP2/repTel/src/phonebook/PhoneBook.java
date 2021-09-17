package phonebook;

import java.util.ArrayList;
import java.util.Objects;

public class PhoneBook {
    ArrayList<Contact> contactList;

    public PhoneBook() {
        this.contactList = new ArrayList<Contact>();  // créé la liste des contacts
    }

    public void addContact(String name, String phoneNumber) {
        Contact zeNewContact = new Contact(name, phoneNumber);  // créé un nouveau contact
        this.contactList.add(zeNewContact);  // ajoute le nouveau contact à la liste
    }

    public ArrayList<String> getPhoneNumbers(String name) {
        ArrayList<String> correspond = new ArrayList<String>();  // stocke les noms correspondants

        for (int i = 0; i < this.contactList.size(); i++) {  // parcours la liste des contacts(méthode 1)
            if (this.contactList.get(i).getName() == name) {  // si le nom du contact i est celui recherché
                correspond.add(this.contactList.get(i).getPhoneNumber());  // l'ajoute aux correspondants
            }
        }
        return correspond;  // retourne la liste
    }

    public ArrayList<String> getNames(String phoneNumber) {
        ArrayList<String> correspond = new ArrayList<String>();  // stocke les numéros correspondants

        for (Contact contact : this.contactList) {  // parcours les contacts(méthode 2)
            if (Objects.equals(contact.getPhoneNumber(), phoneNumber)) {  // si le numéro est celui recherché
                correspond.add(contact.getName());  // l'ajoute à la liste des correspondants
            }
        }
        return correspond;  // retourne la liste
    }

}
