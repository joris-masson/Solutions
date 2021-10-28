package leslistes.exec;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BenchmarkGet {
    public static void bruhIterateur (List<String> listeVideJeCrois, int nbElem) {
        int tailleLongueurChaines = 0;
        for (int i = 0; i < nbElem; i++) {
            listeVideJeCrois.add("element #" + i);
        }
        for (int i = 0; i < listeVideJeCrois.size(); i++) {
            tailleLongueurChaines += listeVideJeCrois.get(i).length();
        }
    }

    public static void bruhMieux (List<String> listeVideJeCrois, int nbElem) {
        int tailleLongueurChaines = 0;
        for (int i = 0; i < nbElem; i++) {
            listeVideJeCrois.add(0, "element #" + i);
        }
        for (String laString: listeVideJeCrois) {
            tailleLongueurChaines += laString.length();
        }
    }

    public static void main(String[] args) {
        final int NB_TESTS = Integer.parseInt(args[0]);
        long debutTest;

        ArrayList<String> listeVide = new ArrayList<>();
        LinkedList<String> listeLieeVide = new LinkedList<>();

        debutTest = System.currentTimeMillis();
        bruhIterateur(listeVide, NB_TESTS);
        System.out.println(System.currentTimeMillis() - debutTest);

        debutTest = System.currentTimeMillis();
        bruhIterateur(listeLieeVide, NB_TESTS);
        System.out.println(System.currentTimeMillis() - debutTest);

        debutTest = System.currentTimeMillis();
        bruhMieux(listeVide, NB_TESTS);
        System.out.println(System.currentTimeMillis() - debutTest);

        debutTest = System.currentTimeMillis();
        bruhMieux(listeLieeVide, NB_TESTS);
        System.out.println(System.currentTimeMillis() - debutTest);
    }
}
