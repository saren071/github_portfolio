"""
This is a cli file utilities.
"""


import os

from utils.os_utils import OSUtils


class FileUtilities:
    """
    This class handles the file utilities.
    """
    def __init__(self):
        """
        This method initializes the file utilities.
        """
        self.os_utils = OSUtils()
        self.boolean_exit_program = False

    def cli_menu(self):
        """
        This will handle the cli display for the utilities.
        """
        print("Welcome to the File Utilities!\n\nPlease select an option to get started!")
        while True:
            print("1. Check system information")
            print("2. Check disk space")
            print("3. Sort files")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.check_system_information()
                continue
            elif choice == "2":
                self.check_disk_space()
                continue
            elif choice == "3":
                self.sort_files()
                continue
            elif choice == "4":
                self.exit_program()
                if self.boolean_exit_program:
                    break
                else:
                    continue
            else:
                print("Invalid choice. Please try again.")
                continue

    def exit_program(self):
        """
        This will handle the exiting of the program.
        """
        self.boolean_exit_program = False
        while not self.boolean_exit_program:
            print("Are you sure you want to exit? (y/n)")
            if input().strip().lower() == "y":
                print("Thank you for using the File Utilities!")
                self.boolean_exit_program = True
            elif input().strip().lower() == "n":
                self.boolean_exit_program = True
            else:
                print("Invalid choice. Please try again.")
                self.boolean_exit_program = False

    def check_system_information(self):
        """
        This will handle the checking of system information.
        """
        print("System information:")
        # TODO: Implement human readable output for the system information and fix multiple statements,
        # like the GPU, the CPU name, the memory size instead of terminal size.
        print(f"Operating system: {self.os_utils.get_operating_system()}")
        print(f"Operating system version: {self.os_utils.get_operating_system_version()}")
        print(f"Operating system architecture: {self.os_utils.get_operating_system_architecture()}")
        print(f"Operating system platform: {self.os_utils.get_operating_system_platform()}")
        print(f"Operating system processor: {self.os_utils.get_operating_system_processor()}")
        print(f"CPU count: {os.cpu_count()}")
        print(f"Memory: {os.get_terminal_size().columns}x{os.get_terminal_size().lines}")
        print(f"GPU: {os.getenv('CUDA_VISIBLE_DEVICES')}")

    def check_disk_space(self):
        """
        This will handle the checking of disk space.
        """
        pass

    def sort_files(self):
        """
        This will handle the sorting of files.
        """
        pass


if __name__ == "__main__":
    file_utilities = FileUtilities()
    file_utilities.cli_menu()
