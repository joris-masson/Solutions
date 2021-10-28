package volumes;

public class Prism extends Figure {
    double basisLength;
    double basisHeight;

    public Prism(double basisLength, double basisHeight, double height) {
        super(height);
        this.basisLength = basisLength;
        this.basisHeight = basisHeight;
        this.height = height;
    }

    public double getBasisLength() {
        return this.basisLength;
    }

    public double getBasisHeight() {
        return this.basisHeight;
    }

    @Override
    public double basisSurface() {
        return (this.basisLength * this.basisHeight) / 2;
    }
}
