package houses;

import java.util.HashSet;

public class Prices {
    float prixIn;
    float prixOut;

    public Prices(float prixIn, float prixOut) {
        this.prixIn = prixIn;
        this.prixOut = prixOut;
    }

    public float getPrice(House maison) {
        return maison.getPrice(this.prixIn, this.prixOut);
    }

    public float getPrice(HashSet<House> beaucoupMaisons) {
        float res = 0;
        for (House maison: beaucoupMaisons) {
            res += maison.getPrice(this.prixIn, this.prixOut);
        }
        return res;
    }
}
