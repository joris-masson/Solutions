package houses;

import housestests.*;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;
        HouseTests houseTester = new HouseTests();
        ok = ok && houseTester.testGetAddress();
        ok = ok && houseTester.testGetPrice();
        VillaTests villaTester=new VillaTests();
        ok = ok && villaTester.testGetAddress();
        ok = ok && villaTester.testGetPrice();
        PricesTests pricesTester=new PricesTests();
        ok = ok && pricesTester.testGetPriceOneHouse();
        ok = ok && pricesTester.testGetPriceSet();
        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
