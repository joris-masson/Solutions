package judges.exec;

import java.util.Arrays;
import java.util.function.IntPredicate;

public class Demo {
    public static void main(String[] args) {
        int unTablo[] = new int[5];
        for (int i = 0; i < 5; i++) {
            unTablo[i] = 2;
            System.out.println(unTablo[i]);
        }

        if (Arrays.stream(unTablo).max().isPresent()) {
            System.out.println(Arrays.stream(unTablo).max().getAsInt());
        } else {
            System.out.println("y a pas de max");
        }

        if (Arrays.stream(unTablo).min().isPresent()) {
            System.out.println(Arrays.stream(unTablo).min().getAsInt());
        } else {
            System.out.println("y a pas de min");
        }
    }
}
