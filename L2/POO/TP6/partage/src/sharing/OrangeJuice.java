package sharing;

public class OrangeJuice implements Sharable {
    float quantity;

    public OrangeJuice(float quantity) {
        this.quantity = quantity;
    }

    public float getQuantity() {
        return this.quantity;
    }

    @Override
    public String toString() {
        float quantity = this.getQuantity();
        if (quantity == 0) {
            return "Le verre est vide";
        } else {
            return String.format("Le verre contient %fcl", quantity);
        }
    }

    @Override
    public Sharable share(int nbPersonnes) {
        float quantityPourChaquePersonne = this.getQuantity() / nbPersonnes;
        return new OrangeJuice(quantityPourChaquePersonne);
    }

    @Override
    public Sharable remainder(int nbPersonnes) {
        return new OrangeJuice(0f);  // il ne peut pas y avoir de reste
    }
}
