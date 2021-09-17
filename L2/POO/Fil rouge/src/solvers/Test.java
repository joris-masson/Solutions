package solvers;

import solverstests.TopologicalSorterTests;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;
        TopologicalSorterTests tester = new TopologicalSorterTests();
        ok = ok && tester.testBruteForceSort();
        // ok = ok && tester.testSchedule();
        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
