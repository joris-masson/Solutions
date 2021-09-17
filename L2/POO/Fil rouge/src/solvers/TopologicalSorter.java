package solvers;

import constraints.Activity;
import constraints.PrecedenceConstraint;

import java.util.ArrayList;
import java.util.HashSet;

public class TopologicalSorter {
    public TopologicalSorter() {

    }

    public ArrayList<Activity> bruteForceSort(HashSet<Activity> activites, HashSet<PrecedenceConstraint> contraintesPreced) {
        // TODO Comprendre
        HashSet<Activity> activitesCopy = activites;
        ArrayList<Activity> res = new ArrayList<Activity>();
        while (!activitesCopy.isEmpty()) {
            boolean continuer = false;
            for (Activity activite: activites) {
                boolean ok = true;
                for (PrecedenceConstraint contrainte: contraintesPreced) {
                    if ((activite != contrainte.getSecond()) && res.contains(contrainte.getSecond())) {
                        ok = false;
                    }
                }
                if (ok) {
                    res.add(activite);
                    activitesCopy.remove(activite);
                    continuer = true;
                    break;
                }
            }
            if (!continuer) {
                return null;
            }
        }
        return res;
    }
}
