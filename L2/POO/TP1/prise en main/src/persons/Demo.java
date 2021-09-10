package persons;

/**
 * An executable class for demonstrating the use of class Person.
 * 
 * @author Bruno Zanuttini, Université de Caen Normandie, France
 */
public class Demo {

	/**
	 * Runs a demo of class Person.
	 * 
	 * @param args ignored
	 */
	public static void main(String[] args) {

		Person jean = new Person("Jean Martin", 2000, 1, 1);
		System.out.println(jean.getPresentation());

		Person marie = new Person("Marie Dupont", 1999, 12, 31);
		int futureYear = 2050;
		int futureMonth = 3;
		int futureDay = 1;
		int futureAge = marie.getAge(futureYear, futureMonth, futureDay);
		System.out.println(marie.getPresentation());
		String futureDate = futureYear + "-" + futureMonth + "-" + futureDay;
		System.out.println("On " + futureDate + ", I will be " + futureAge + " years old.");

	}

}
