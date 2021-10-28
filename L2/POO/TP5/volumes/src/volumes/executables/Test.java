package volumes.executables;

import volumestests.*;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;

        ParallelepipedTests parallelepipedTester = new ParallelepipedTests();

        ok = ok && parallelepipedTester.testGetHeight();
        ok = ok && parallelepipedTester.testGetLength();
        ok = ok && parallelepipedTester.testGetWidth();
        ok = ok && parallelepipedTester.testBasisSurface();
        ok = ok && parallelepipedTester.testVolume();
        ok = ok && parallelepipedTester.testExtends();

        CylinderTests cylinderTester = new CylinderTests();
        ok = ok && cylinderTester.testGetHeight();
        ok = ok && cylinderTester.testGetRadius();
        ok = ok && cylinderTester.testBasisSurface();
        ok = ok && cylinderTester.testVolume();
        ok = ok && cylinderTester.testExtends();

        PrismTests prismTester = new PrismTests();
        ok = ok && prismTester.testGetHeight();
        ok = ok && prismTester.testGetBasisHeight();
        ok = ok && prismTester.testGetBasisLength();
        ok = ok && prismTester.testBasisSurface();
        ok = ok && prismTester.testVolume();
        ok = ok && prismTester.testExtends();

        CubeTests cubeTester = new CubeTests();
        ok = ok && cubeTester.testGetHeight();
        ok = ok && cubeTester.testGetLength();
        ok = ok && cubeTester.testGetWidth();
        ok = ok && cubeTester.testGetEdgeSize();
        ok = ok && cubeTester.testBasisSurface();
        ok = ok && cubeTester.testVolume();
        ok = ok && cubeTester.testExtends();

        FigureTests figureTester = new FigureTests();
        ok = ok && figureTester.testGetHeight();
        ok = ok && figureTester.testVolume();

        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
