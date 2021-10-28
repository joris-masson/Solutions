package stacks.executables;

import stackstests.*;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;

        BoxTests boxTester = new BoxTests();
        ok = ok && boxTester.testGetLength();
        ok = ok && boxTester.testGetWidth();
        ok = ok && boxTester.testGetHeight();

        ArtWorkTests artworkTester = new ArtWorkTests();
        ok = ok && artworkTester.testGetAuthor();
        ok = ok && artworkTester.testGetTitle();

        BookTests bookTester = new BookTests();
        ok = ok && bookTester.testGetAuthor();
        ok = ok && bookTester.testGetTitle();
        ok = ok && bookTester.testGetHeight();

        PaintingTests paintingTester = new PaintingTests();
        ok = ok && paintingTester.testGetAuthor();
        ok = ok && paintingTester.testGetTitle();

        BoxedPaintingTests boxedPaintingTester = new BoxedPaintingTests();
        ok = ok && boxedPaintingTester.testGetBox();
        ok = ok && boxedPaintingTester.testGetPainting();
        ok = ok && boxedPaintingTester.testGetHeight();

        StackTests stackTester = new StackTests();
        ok = ok && stackTester.testAddObjectAndNbObjects();
        ok = ok && stackTester.testGetTotalHeight();

        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
