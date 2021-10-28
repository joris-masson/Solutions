package sharing.executables;

import sharingtests.MarbleBagTests;
import sharingtests.OrangeJuiceTests;
import sharingtests.SetOfGoodsTests;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;
        MarbleBagTests marbleTester = new MarbleBagTests();
        ok = ok && marbleTester.testShare();
        ok = ok && marbleTester.testRemainder();
        OrangeJuiceTests orangeJuiceTester = new OrangeJuiceTests();
        ok = ok && orangeJuiceTester.testShare();
        ok = ok && orangeJuiceTester.testRemainder();
        SetOfGoodsTests setOfGoodsTester = new SetOfGoodsTests();
        ok = ok && setOfGoodsTester.testAddGoodAndGetGoods();
        ok = ok && setOfGoodsTester.testShare();
        ok = ok && setOfGoodsTester.testRemainder();
        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
