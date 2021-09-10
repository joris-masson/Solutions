package geometry;

public class Position {
	int x;
	int y;

	public Position(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return this.x;
	}

	public int getY() {
		return this.y;
	}

	public String getRepresentation() {
		String x = String.valueOf(this.getX());
		String y = String.valueOf(this.getY());
		String laPosition = '(' + x + ',' + y + ')';
		return laPosition;
	}

	public Position symmetricX() {
		Position symmX = new Position(this.x, -this.y);
		return symmX;
	}

	public void translate(int deltaX, int deltaY) {
		this.x += deltaX;
		this.y += deltaY;
	}
}