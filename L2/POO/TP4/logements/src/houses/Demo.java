package houses;

public class Demo {
    public static void main(String[] args) {
        final float PRIX_METRE_CARRE_INTERIEUR = (float) 66.6;
        final float PRIX_METRE_CARRE_EXTERIEUR = (float) 99.9;

        // ----- démo pour les maisons -----
        House uneMaison = new House("177013, rue des hentai", 69);
        House uneAutreMaison = new House("228922, boulevard des atrocités", 42);

        System.out.println(uneMaison);
        System.out.println(uneMaison.getPrice(PRIX_METRE_CARRE_INTERIEUR, PRIX_METRE_CARRE_EXTERIEUR) + "€");

        System.out.println(uneAutreMaison);
        System.out.println(uneAutreMaison.getPrice(PRIX_METRE_CARRE_INTERIEUR, PRIX_METRE_CARRE_EXTERIEUR) + "€");

        System.out.println("ça fait beaucoup non?");

        // ----- démo pour les villas -----
        Villa uneVilla = new Villa("69, allée du segs", 375, 666);

        System.out.println(uneVilla);
        System.out.println(uneVilla.getPrice(PRIX_METRE_CARRE_INTERIEUR, PRIX_METRE_CARRE_EXTERIEUR) + "€");
    }
}
