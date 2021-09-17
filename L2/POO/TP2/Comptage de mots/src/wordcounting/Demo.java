package wordcounting;

import java.util.ArrayList;
import java.util.Arrays;

public class Demo {
    public static void main(String[] args) {
        ArrayList<String> sentence = new ArrayList<>(Arrays.asList(args));
        WordCounter zeWordCounter = new WordCounter(false);
        System.out.println(zeWordCounter.words(sentence));
        System.out.println(zeWordCounter.count(sentence));
    }
}
