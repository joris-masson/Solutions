package volumes;

public class Cube extends Parallelepiped {
    double longueur;

    public Cube(double longueur) {
        super(longueur, longueur, longueur);
        this.longueur = longueur;
    }

    public double getEdgeSize() {
        return longueur;
    }
}
