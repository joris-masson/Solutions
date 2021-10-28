package sharing;

public class MarbleBag implements Sharable {
    int nbMarbles;

    public MarbleBag(int nbBilles) {
        this.nbMarbles = nbBilles;
    }

    public int getNbMarbles() {
        return this.nbMarbles;
    }

    @Override
    public String toString() {
        int nbMarbles = this.getNbMarbles();
        if (nbMarbles == 0) {
            return "Le sac est vide";
        } else if (nbMarbles == 1) {
            return "Sac de 1 bille";
        } else {
            return String.format("Sac de %d billes", nbMarbles);
        }
    }

    @Override
    public Sharable share(int nbPersonnes) {
        int nbPourChacun = this.getNbMarbles() / nbPersonnes;
        return new MarbleBag(nbPourChacun);
    }

    @Override
    public Sharable remainder(int nbPersonnes) {
        int nbRestant = this.getNbMarbles() % nbPersonnes;
        return new MarbleBag(nbRestant);
    }
}
