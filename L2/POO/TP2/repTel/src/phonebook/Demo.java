package phonebook;

public class Demo {
    public static void main(String[] args) {
        PhoneBook zePhoneBook = new PhoneBook();
        zePhoneBook.addContact("moi", "0664501619");
        zePhoneBook.addContact("hen", "177013");
        zePhoneBook.addContact("hen", "228922");
        zePhoneBook.addContact("Un imposteur", "0664501619");

        System.out.println(zePhoneBook.getPhoneNumbers("hen"));
        System.out.println(zePhoneBook.getNames("0664501619"));

    }
}
