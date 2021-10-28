package volumes;

public class Cylinder extends Figure {
    double radius;

    public Cylinder(double radius, double height) {
        super(height);
        this.radius = radius;
    }

    public double getRadius() {
        return this.radius;
    }

    @Override
    public double basisSurface() {
        return Math.PI * (Math.pow(radius, 2));
    }

}
