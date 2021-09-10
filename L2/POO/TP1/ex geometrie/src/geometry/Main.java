package geometry;

import geometrytests.PositionTests;
import geometrytests.SegmentTests;

public class Main {
	public static void main(String[] args) {
		// ----- position -----
		Position machin = new Position(3, 4);  // nouvelle instance de Position avec x = 3 et y = 4
		System.out.println(machin.getX());  // affiche le x de machin
		System.out.println(machin.getY());  // affiche le y de machin
		System.out.println(machin.getRepresentation());  // affiche les coordonnées de machin sous forme (x,y)

		Position symmMachin = machin.symmetricX();  // créé une nouvelle instance de Position, mais avec le symmetrique de machin
		System.out.println(symmMachin.getRepresentation());  // affiche ses coordonnées

		machin.translate(2, 2);  // ajoute 2 à x et y de machin
		System.out.println(machin.getRepresentation());  // affiche les coordonnées de machin

		// ----- test position -----
		boolean ok = true;
		PositionTests positionTester = new PositionTests();
		ok = ok && positionTester.testGetX();
		ok = ok && positionTester.testGetY();
		ok = ok && positionTester.testSymmetricX();
		ok = ok && positionTester.testTranslate();
		System.out.println(ok ? "All tests passed" : "At least one test failed");

		// ----- segment -----
		Segment zeSegment = new Segment(machin, symmMachin);  // créé une nouvelle instance de Segment avec comme points machin et son symmetrique
		System.out.println(zeSegment.getRepresentation());  // affiche les coordonnées des deux points
		machin.translate(-2, -2); // repasse à l'ancienne position du point machin
		Position point2 = new Position(7, 7);  // créé un nouveau point en (7,7)
		Segment zeSecondSegment = new Segment(machin, point2);  // créé un nouveau Segment avec machin et point2
		System.out.println(zeSecondSegment.getRepresentation());  // affiche les coordonnées
		System.out.println(zeSecondSegment.length());  // affiche sa longueur

		// ----- test segment -----
		boolean ok2 = true;
		SegmentTests segmentTester = new SegmentTests();
		ok2 = ok2 && segmentTester.testLength();
		System.out.println(ok2 ? "All tests passed" : "At least one test failed");
	}
}