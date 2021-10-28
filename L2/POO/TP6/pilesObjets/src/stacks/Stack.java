package stacks;

import java.util.ArrayList;

public class Stack {
    ArrayList<Stackable> stack;

    public Stack() {
        this.stack = new ArrayList<>();
    }

    public ArrayList<Stackable> getStack() {
        return this.stack;
    }

    public void addObject(Stackable object) {
        this.getStack().add(object);
    }

    public int nbObjects() {
        return this.getStack().size();
    }

    public float getTotalHeight() {
        float totalHeight = 0;

        for (Stackable boite: this.getStack()) {
            totalHeight += boite.getHeight();
        }
        return totalHeight;
    }
}
