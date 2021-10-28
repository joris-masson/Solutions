package volumes.executables;

import volumes.*;

public class Demo {
    public static void afficheDetails(Figure laFigure) {
        double basisSurface = laFigure.basisSurface();
        double height = laFigure.getHeight();
        double volume = laFigure.volume();
        System.out.printf("La surface de la base est: %f\nLa hauteur est: %f\nLe volume est: %f\n\n", basisSurface, height, volume);
    }

    public static void main(String[] args) {
        Parallelepiped unParallelepiped = new Parallelepiped(4.5, 3.9, 177.013);
        Cylinder unCylindre = new Cylinder(177.0, 2289.22);
        Prism unPrisme = new Prism(2.0, 1.0, 15.0);
        Cube unCube = new Cube(40.0);

        afficheDetails(unParallelepiped);
        afficheDetails(unCylindre);
        afficheDetails(unPrisme);
        afficheDetails(unCube);
    }
}
