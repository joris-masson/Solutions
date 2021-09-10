package persons;

// For retrieving the current date
import java.util.Calendar;
import java.util.GregorianCalendar;

/**
 * A class for representing persons with a name and a birth date.
 * <p>
 * Note: this class uses three integers for representing the birth date, but it
 * may be interesting to implement a version using java.util.GregorianCalendar.
 * 
 * @author Bruno Zanuttini, Université de Caen Normandie, France
 */
public class Person {

	/** The person's name. */
	private String name;

	/** The year when the person was born. */
	private int birthYear;

	/** The month when the person was born (1 for January, ..., 12 for December). */
	private int birthMonth;

	/** The day in the month when the person was born (1 to 31). */
	private int birthDay;

	/**
	 * Builds a new person. Note that no verification is made of the validity of the
	 * birth date.
	 * 
	 * @param name       The person's name
	 * @param birthYear  The year when the person was born
	 * @param birthMonth The month when the person was born (1 for January, ..., 12
	 *                   for December)
	 * @param birthDay   The day in the month when the person was born (1 to 31)
	 */
	public Person(String name, int birthYear, int birthMonth, int birthDay) {
		this.name = name;
		this.birthYear = birthYear;
		this.birthMonth = birthMonth;
		this.birthDay = birthDay;
	}

	/**
	 * Returns an English sentence for the person to introduce herself.
	 * 
	 * @return An English sentence for the person to introduce herself
	 */
	public String getPresentation() {
		return "I am " + this.name + ", born " + this.birthDateToString() + ", and I am " + this.getCurrentAge()
				+ " years old.";
	}

	/**
	 * Returns this person's age at a given date. Note that no verification is made
	 * of the validity of the given year.
	 * 
	 * @param year  The year when to evaluate the person's age
	 * @param month The month when to evaluate the person's age (1 for January, ...,
	 *              12 for December)
	 * @param day   The day in the month when to evaluate the person's age (1 to 31)
	 * @return This person's age at the given date
	 */
	public int getAge(int year, int month, int day) {
		// Decide whether birthday is over in the current year
		boolean birthdayOver = false;
		if (this.birthMonth < month) {
			birthdayOver = true;
		} else if (this.birthMonth == month && this.birthDay <= day) {
			birthdayOver = true;
		}
		// Correct difference between years as necessary
		if (birthdayOver) {
			return year - this.birthYear;
		} else {
			return year - this.birthYear - 1;
		}
	}

	/**
	 * Returns this person's age at the current date.
	 * 
	 * @return This person's age at the current date
	 */
	public int getCurrentAge() {
		GregorianCalendar now = new GregorianCalendar();
		int year = now.get(Calendar.YEAR);
		// Month needs to be corrected since 0 encodes January
		// in class java.util.GregorianCalendar
		int month = now.get(Calendar.MONTH) + 1;
		int day = now.get(Calendar.DAY_OF_MONTH);
		return this.getAge(year, month, day);
	}

	/**
	 * Returns a string representing this person's birth date.
	 * 
	 * @return A string representing this person's birth date
	 */
	public String birthDateToString() {
		return this.birthYear + "-" + this.birthMonth + "-" + this.birthDay;
	}

}
