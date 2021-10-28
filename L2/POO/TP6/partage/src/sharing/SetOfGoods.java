package sharing;

import java.util.ArrayList;

public class SetOfGoods implements Sharable {
    ArrayList<Sharable> goods;

    public SetOfGoods() {
        this.goods = new ArrayList<>();
    }

    public void addGood(Sharable good) {
        this.goods.add(good);
    }

    public ArrayList<Sharable> getGoods() {
        return this.goods;
    }

    @Override
    public Sharable share(int nbPersonnes) {
        SetOfGoods unSetDepartage = new SetOfGoods();
        for (Sharable unItemAPartager : this.goods) {
            unSetDepartage.addGood(unItemAPartager.share(nbPersonnes));
        }
        return unSetDepartage;
    }

    @Override
    public Sharable remainder(int nbPersonnes) {
        SetOfGoods unSetRestant = new SetOfGoods();
        for (Sharable unItemAPartager : this.goods) {
            unSetRestant.addGood(unItemAPartager.remainder(nbPersonnes));
        }
        return unSetRestant;
    }

    @Override
    public String toString() {
        return this.getGoods().toString();
    }
}
