package houses;

public class Villa extends House{
    String adresse;
    int surfaceIn;
    int surfaceOut;

    public Villa(String adresse, int surfaceIn, int surfaceOut) {
        super(adresse, surfaceIn);
        this.adresse = adresse;
        this.surfaceIn = surfaceIn;
        this.surfaceOut = surfaceOut;
    }

    @Override
    public float getPrice(float prixMetreCarreIn, float prixMetreCarreOut) {
        float resIn = this.surfaceIn * prixMetreCarreIn;
        float resOut = this.surfaceOut * prixMetreCarreOut;

        return resIn + resOut;
    }

    @Override
    public String toString() {
        return adresse + ", " + this.surfaceIn + "m², " + this.surfaceOut + "m²";
    }
}
