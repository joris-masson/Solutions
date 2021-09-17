package constraints;

// ----- importations -----
import constraintstests.ActivityTests;
import constraintstests.PrecedenceConstraintTests;
import constraintstests.MeetConstraintTests;

public class Main {
	public static void main(String[] args) {
		Activity uneActivite = new Activity("rule", 34);  // instancie une activité
		System.out.println(uneActivite.getDescription());  // affiche sa description
		System.out.println(uneActivite.getDuration());  // affiche sa durée

		// ----- test Activity -----
		boolean ok = true;
		ActivityTests activityTester = new ActivityTests();
		ok = ok && activityTester.testGetDescription();
		ok = ok && activityTester.testGetDuration();
		System.out.println(ok ? "All tests passed" : "At least one test failed");

		// ----- PrecedenceConstraint -----
		Activity act1 = new Activity("la premiere!", 15);
		Activity act2 = new Activity("la deuxieme!", 2);

		PrecedenceConstraint unTruc = new PrecedenceConstraint(act1, act2);
		System.out.print("Avec 5 et 20: ");
		System.out.println(unTruc.isSatisfied(5, 20));
		System.out.print("Avec 5 et 18: ");
		System.out.println(unTruc.isSatisfied(5, 18));

		// ----- test PrecedenceConstraint -----
		PrecedenceConstraintTests precedenceConstraintTester = new PrecedenceConstraintTests();
		ok = ok && precedenceConstraintTester.testGetFirst();
		ok = ok && precedenceConstraintTester.testGetSecond();
		ok = ok && precedenceConstraintTester.testIsSatisfiedBy();
		System.out.println(ok ? "All tests passed" : "At least one test failed");

		// ----- test MeetConstraints -----
		MeetConstraintTests meetConstraintTester = new MeetConstraintTests();  
		ok = ok && meetConstraintTester.testGetFirst();
		ok = ok && meetConstraintTester.testGetSecond();
		ok = ok && meetConstraintTester.testIsSatisfiedBy();
		System.out.println(ok ? "All tests passed" : "At least one test failed");
	}
}