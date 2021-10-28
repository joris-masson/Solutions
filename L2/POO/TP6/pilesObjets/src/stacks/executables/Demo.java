package stacks.executables;

import stacks.*;

public class Demo {
    public static void main(String[] args) {
        Box uneBoite = new Box(76, 1, 56);
        Book unLivre = new Book("Adolf Hitler", "Mein Kampf", 688);
        Painting unePeinture = new Painting("Adolf Hitler", "Der Alte Hof in München");
        BoxedPainting unePeintureEnBoite = new BoxedPainting(unePeinture, uneBoite);

        Stack unStack = new Stack();
        unStack.addObject(unePeintureEnBoite);
        unStack.addObject(unLivre);

        System.out.println(unStack.getTotalHeight());
    }
}
