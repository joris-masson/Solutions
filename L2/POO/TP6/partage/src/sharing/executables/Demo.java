package sharing.executables;

import com.sun.org.apache.xpath.internal.operations.Or;
import sharing.MarbleBag;
import sharing.OrangeJuice;
import sharing.SetOfGoods;

public class Demo {
    public static void main(String[] args) {
        MarbleBag unSacDeBilles = new MarbleBag(20);
        OrangeJuice unJusDOrange = new OrangeJuice(20.0f);

        System.out.println(unSacDeBilles);
        System.out.println(unJusDOrange);

        System.out.println(unSacDeBilles.share(3));
        System.out.println(unSacDeBilles.remainder(3));

        System.out.println(unJusDOrange.share(3));
        System.out.println(unJusDOrange.remainder(3));

        SetOfGoods unSet = new SetOfGoods();
        unSet.addGood(unSacDeBilles);
        unSet.addGood(unJusDOrange);

        System.out.println(unSet);
    }
}
