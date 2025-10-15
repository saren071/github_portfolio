import random


class RandomNumberGenerator:
    """
    A simple command-line random number generator.
    """
    def __init__(self):
        """Initialize the random number generator."""
        self.precision = 2
        self.float_int = False

    def cli_menu(self):
        """Display the main CLI menu."""
        print("Welcome to the Random Number Generator!\n")

        while True:
            print("1. Generate a random number")
            print("2. Options")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.generate_random_number()
            elif choice == "2":
                self.options()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

    def generate_random_number(self):
        """Generate and display a random number between two user inputs."""
        while True:
            try:
                if self.float_int:
                    num1 = int(input("Enter the first number: "))
                    num2 = int(input("Enter the second number: "))
                else:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))

                if num1 == num2:
                    print("Numbers must be different. Try again.\n")
                    continue

                random_number = random.uniform(min(num1, num2), max(num1, num2))
                if self.float_int:
                    random_number = int(random_number)
                else:
                    random_number = float(random_number)
                if self.float_int:
                    print(f"Your random number: {random_number}\n")
                else:
                    print(f"Your random number: {random_number:.{self.precision}f}\n")
            except ValueError:
                print("Invalid input. Please enter valid numbers.\n")
                continue

            again = input("Generate another? (y/n): ").strip().lower()
            if again != "y":
                print()
                break

    def set_precision(self):
        """Set the precision of the random number."""
        print("Set precision:")
        try:
            precision = int(input("Enter the precision: ").strip())
        except ValueError:
            print("Precision must be a number. Try again.\n")
            return
        if precision < 0:
            print("Precision must be greater than or equal to 0. Try again.\n")
            return
        elif precision > 10:
            print("Precision must be less than or equal to 10. Try again.\n")
            return
        self.precision = precision
        print(f"Precision set to {precision}. \n")

    def toggle_float_int(self):
        """Toggle between float and int."""
        self.float_int = not self.float_int
        if self.float_int:
            print("Switched to integer mode. \n")
        else:
            print("Switched to float mode. \n")

    def options(self):
        """Display the options menu."""
        print("=== Options ===")
        print(f"Current mode: {'Integer' if self.float_int else 'Float'}")
        print(f"Current precision: {self.precision}")
        print("1. Set precision")
        print("2. Toggle between float and int")
        print("3. Back")
        print()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            if self.float_int:
                print("You must toggle to float mode first. \n")
                return
            else:
                self.set_precision()
        elif choice == "2":
            self.toggle_float_int()
        elif choice == "3":
            return


if __name__ == "__main__":
    rng = RandomNumberGenerator()
    rng.cli_menu()
