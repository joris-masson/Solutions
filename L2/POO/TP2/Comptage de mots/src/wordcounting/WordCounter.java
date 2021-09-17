package wordcounting;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class WordCounter {
    boolean isSensible;

    public WordCounter(boolean isSensible) {
        this.isSensible = isSensible;
    }

    public HashSet<String> words(ArrayList<String> phrase) {
        HashSet<String> lesMots = new HashSet<String>();
        if (this.isSensible) {
            lesMots.addAll(phrase);
        } else {
            for (String mot: phrase) {
                lesMots.add(mot.toLowerCase());
            }
        }

        return lesMots;
    }

    public HashMap<String, Integer> count(ArrayList<String> phrase) {
        HashMap<String, Integer> compte = new HashMap<String, Integer>();
        HashSet<String> lesMots = this.words(phrase);

        for (String mot : lesMots) {
            compte.put(mot, 0);
        }

        if (this.isSensible) {
            for (String mot : phrase) {
                Integer val = compte.get(mot);
                compte.put(mot, val + 1);
            }
        } else {
            for (String mot : phrase) {
                Integer val = compte.get(mot.toLowerCase());
                compte.put(mot.toLowerCase(), val + 1);
            }
        }
        return compte;
    }
}
