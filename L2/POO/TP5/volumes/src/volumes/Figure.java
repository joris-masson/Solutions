package volumes;

public abstract class Figure {
    protected double height;

    public Figure(double hauteur) {
        this.height = hauteur;
    }

    public double getHeight() {
        return this.height;
    }

    public abstract double basisSurface();

    public double volume() {
        return this.basisSurface() * this.height;
    }
}
