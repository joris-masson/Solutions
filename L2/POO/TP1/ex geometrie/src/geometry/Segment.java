package geometry;

public class Segment {
	Position pos1;
	Position pos2;

	public Segment(Position pos1, Position pos2) {
		this.pos1 = pos1;
		this.pos2 = pos2;
	}

	public String getRepresentation() {
		String zePos1 = this.pos1.getRepresentation();
		String zePos2 = this.pos2.getRepresentation();

		String zeString = zePos1 + " - " + zePos2;

		return zeString;
	}

	public double length() {
		return Math.sqrt(Math.pow((this.pos1.getX()-this.pos2.getX()), 2)+Math.pow((this.pos1.getY()-this.pos2.getY()), 2));
	}

}