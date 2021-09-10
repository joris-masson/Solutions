package persons;

import personstests.PersonTests;

/**
 * Executable class for testing package persons.
 * 
 * @author Bruno Zanuttini, Université de Caen Normandie, France
 */
public class Test {

	/**
	 * Runs the tests and logs the results to standard output.
	 * 
	 * @param args ignored
	 */
	public static void main(String[] args) {
		PersonTests tester = new PersonTests();
		boolean ok = true;
		ok = ok && tester.testGetAge();
		ok = ok && tester.testGetCurrentAge();
		System.out.println(ok ? "All tests passed" : "At least one test failed");
	}

}
