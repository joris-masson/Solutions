package exoEquals;

import java.util.Objects;

public class PersonWithEquality extends Person {
    public PersonWithEquality(String firstName, String lastName) {
        super(firstName, lastName);
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof PersonWithEquality)) {
            return false;
        } else {
            boolean prem = this.getFirstName().equals(((PersonWithEquality) o).getFirstName());
            boolean deux = this.getLastName().equals(((PersonWithEquality) o).getLastName());
            return prem && deux;
        }
    }

    @Override
    public int hashCode() {
        int res = 1;
        res += this.getFirstName().hashCode();
        res += this.getLastName().hashCode();
        return res;
    }
}
