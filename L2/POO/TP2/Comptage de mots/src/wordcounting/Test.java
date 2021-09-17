package wordcounting;

import wordcountingtests.WordCounterTests;

import java.util.ArrayList;
import java.util.HashSet;

public class Test {
    public static void main(String[] args) {
        // ----- tests perso -----
        ArrayList<String> unePhrase= new ArrayList<String>();
        unePhrase.add("lol");
        unePhrase.add("LoL");
        unePhrase.add("LOLI");
        unePhrase.add("lol");
        unePhrase.add("LOLI");

        WordCounter tests = new WordCounter(false);
        System.out.println(tests.words(unePhrase));
        System.out.println(unePhrase);
        System.out.println(tests.count(unePhrase));

        // ----- tests -----
        boolean ok = true;
        WordCounterTests tester = new WordCounterTests();
        ok = ok && tester.testWordsCaseSensitive();
        ok = ok && tester.testWordsCaseInsensitive();
        ok = ok && tester.testCountCaseSensitive();
        ok = ok && tester.testCountCaseInsensitive();
        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
