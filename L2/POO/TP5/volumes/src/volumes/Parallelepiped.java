package volumes;

public class Parallelepiped extends Figure {
    double largeur;
    double longueur;

    public Parallelepiped(double largeur, double longueur, double height) {
        super(height);
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public double getWidth() {
        return this.largeur;
    }

    public double getLength() {
        return this.longueur;
    }

    @Override
    public double basisSurface() {
        return this.largeur * this.longueur;
    }
}
