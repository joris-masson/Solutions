package constraints;

public class Activity {
	String description;  // sa description
	int duration;  // sa durée

	public Activity(String description, int duration) {
		this.description = description;
		this.duration = duration;
	}

	public String getDescription() {
		return this.description;
	}

	public int getDuration() {
		return this.duration;
	}
}