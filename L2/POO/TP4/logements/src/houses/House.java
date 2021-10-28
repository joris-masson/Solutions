package houses;

public class House {
    String adresse;
    int surfaceIn;

    public House(String adresse, int surfaceIn) {
        this.adresse = adresse;
        this.surfaceIn = surfaceIn;
    }

    public String getAddress() {
        return adresse;
    }

    public float getPrice(float prixMetreCarreIn, float prixMetreCarreOut) {
        return prixMetreCarreIn * this.surfaceIn;
    }

    @Override
    public String toString() {
        return adresse + ", " + this.surfaceIn + "m²";
    }
}
