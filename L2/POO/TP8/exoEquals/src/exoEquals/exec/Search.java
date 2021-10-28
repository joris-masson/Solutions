package exoEquals.exec;

import exoEquals.Person;

import java.util.ArrayList;
import java.util.List;

public class Search {
    public static void main(String[] args) {
        String firstName = args[0];
        String lastName = args[1];

        System.out.printf("first name: %s\nlast name: %s\n", firstName, lastName);

        Person uneInstanceP = new Person(firstName, lastName);

        List<Person> uneListeDePersonnes = new ArrayList<>();
        uneListeDePersonnes.add(new Person("Adolf", "Hitler"));
        uneListeDePersonnes.add(new Person("Joseph", "Staline"));
        uneListeDePersonnes.add(new Person("Benito", "Mussolini"));

        if (uneListeDePersonnes.contains(uneInstanceP)) {
            System.out.println("Cette personne est connue");
        } else {
            System.out.println("Cette personne est inconnue");
        }

    }
}
