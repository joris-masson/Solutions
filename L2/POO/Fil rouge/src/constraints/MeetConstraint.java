package constraints;

public class MeetConstraint {
	Activity firstActivity;  // bon
	Activity secondActivity;  // j'ai vraiment besoin de le marquer à nouveau?

	public MeetConstraint(Activity firstActivity, Activity secondActivity) {
		this.firstActivity = firstActivity;
		this.secondActivity = secondActivity;
	}

	public Activity getFirst() {
		return this.firstActivity;
	}

	public Activity getSecond() {
		return this.secondActivity;
	}

	public boolean isSatisfied(int date1, int date2) {
		int firstActivityDuration = this.firstActivity.getDuration();
		
		if (firstActivityDuration + date1 == date2) {
			return true;
		} else {
			return false;
		}
	}
}