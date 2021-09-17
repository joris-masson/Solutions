package phonebook;

import phonebooktests.PhoneBookTests;

public class Test {
    public static void main(String[] args) {
        boolean ok = true;
        PhoneBookTests phoneBookTester = new PhoneBookTests();
        ok = ok && phoneBookTester.testGetPhoneNumbers();
        ok = ok && phoneBookTester.testGetNames();
        System.out.println(ok ? "All tests passed" : "At least one test failed");
    }
}
