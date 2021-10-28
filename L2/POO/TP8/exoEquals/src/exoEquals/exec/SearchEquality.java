package exoEquals.exec;

import exoEquals.Person;
import exoEquals.PersonWithEquality;

import java.util.ArrayList;
import java.util.List;

public class SearchEquality {
    public static void main(String[] args) {
        String firstName = args[0];
        String lastName = args[1];

        System.out.printf("first name: %s\nlast name: %s\n", firstName, lastName);

        Person uneInstanceP = new PersonWithEquality(firstName, lastName);

        List<Person> uneListeDePersonnes = new ArrayList<>();
        uneListeDePersonnes.add(new PersonWithEquality("Adolf", "Hitler"));
        uneListeDePersonnes.add(new PersonWithEquality("Joseph", "Staline"));
        uneListeDePersonnes.add(new PersonWithEquality("Benito", "Mussolini"));

        if (uneListeDePersonnes.contains(uneInstanceP)) {
            System.out.println("Cette personne est connue");
        } else {
            System.out.println("Cette personne est inconnue");
        }

    }
}
