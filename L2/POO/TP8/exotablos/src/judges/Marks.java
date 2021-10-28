package judges;

import java.util.Arrays;

public class Marks {
    int nbJudges, nbCriteres, maxNoteAllowed;
    int[][] tableauNotes;

    public Marks(int nbJudges, int nbCriteres, int maxNoteAllowed) {
        this.nbJudges = nbJudges;
        this.nbCriteres = nbCriteres;
        this.maxNoteAllowed = maxNoteAllowed;
        this.tableauNotes = new int[nbJudges][nbCriteres];
    }

    public void setMark(int numJudge, int numCritere, int note) {
        this.tableauNotes[numJudge][numCritere] = note;
    }

    public int getMark(int numJudge, int numCritere) {
        return this.tableauNotes[numJudge][numCritere];
    }

    private boolean isTousLeMeme(int nbATester, int[] liste) {
        for (int nb: liste) {
            if (nb != nbATester) {
                return false;
            }
        }
        return true;
    }

    public float average(int numCritere) {
        int notesCritere = 0;
        int nbNotesPrisesEnComptes = this.nbJudges;
        int[] lesNotes = new int[nbNotesPrisesEnComptes];
        float res = 0f;
        for (int i = 0; i < this.tableauNotes.length; i++) {
            lesNotes[i] = this.tableauNotes[i][numCritere];
        }
        int max = Arrays.stream(lesNotes).max().isPresent() ? Arrays.stream(lesNotes).max().getAsInt() : null;
        int min = Arrays.stream(lesNotes).min().isPresent() ? Arrays.stream(lesNotes).min().getAsInt() : null;

        if (this.isTousLeMeme(max, lesNotes) || this.isTousLeMeme(min, lesNotes)) {
            for (int note: lesNotes) {
                notesCritere += note;
            }
        } else {
            for (int note: lesNotes) {
                if (note == max || note == min) {
                    nbNotesPrisesEnComptes--;
                } else {
                    notesCritere += note;
                }
            }
        }
        res += (float)notesCritere / nbNotesPrisesEnComptes;
        return res;
    }

    public float globalAverage() {
        float res = 0f;
        for (int i = 0; i < this.tableauNotes[nbCriteres].length; i++) {
            res += this.average(i);
        }
        return res / this.tableauNotes[nbCriteres].length;
    }
}
