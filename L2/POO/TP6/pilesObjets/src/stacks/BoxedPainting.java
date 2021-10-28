package stacks;

public class BoxedPainting implements Stackable {
    Painting painting;
    Box box;

    public BoxedPainting(Painting painting, Box box) {
        this.painting = painting;
        this.box = box;
    }

    public Painting getPainting() {
        return this.painting;
    }

    public Box getBox() {
        return this.box;
    }

    @Override
    public float getHeight() {
        return this.getBox().getHeight();
    }
}
