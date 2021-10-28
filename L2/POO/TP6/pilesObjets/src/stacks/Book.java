package stacks;

public class Book extends Artwork implements Stackable{
    public static final float PAGE_HEIGHT = 0.01f;

    protected int nbPages;

    public Book(String author, String title, int nbPages) {
        super(author, title);
        this.nbPages = nbPages;
    }

    public int getNbPages() {
        return this.nbPages;
    }

    @Override
    public float getHeight() {
        return nbPages * PAGE_HEIGHT;
    }
}
