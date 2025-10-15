"""
This is a cli file organizer.
"""
# TODO: Finish the file organizer logic.


class FileOrganizer:
    """
    This class handles the file organizer.
    """
    def __init__(self):
        """
        This method initializes the file organizer.
        """
        pass

    def cli_menu(self):
        """
        This will handle the cli display for the organizer.
        """
        print("Welcome to the File Organizer!\n\nPlease select an option to get started!")
        while True:
            print("1. Organize files")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("this is a test message for choice 1")
                continue
            elif choice == "2":
                print("this is a test message for choice 2")
                break
            else:
                print("Invalid choice. Please try again.")
                continue


if __name__ == "__main__":
    file_organizer = FileOrganizer()
    file_organizer.cli_menu()
