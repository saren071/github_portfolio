"""
This is the magic eight ball project.
"""

import random

from responses import responses


class MagicEightBall:
    """
    This class handles the magic eight ball.
    """
    def __init__(self):
        """
        This method initializes the magic eight ball.
        """
        self.responses = responses

    def cli_menu(self):
        """
        This method handles the cli menu for the magic eight ball.
        """
        print("Welcome to the Magic Eight Ball!")
        while True:
            print("1. Ask a question")
            print("2. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.ask_question()
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                continue

    def ask_question(self):
        """
        This method handles the asking of a question.
        """
        question = input("Enter your question: ").strip()
        if question == "":
            print("Please enter a question.")
            return
        print(random.choice(self.responses))
        while True:
            again = input("Ask another question? (y/n): ").strip().lower()
            if again == "y":
                self.ask_question()
            elif again == "n":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                return


if __name__ == "__main__":
    magic_eight_ball = MagicEightBall()
    magic_eight_ball.cli_menu()
