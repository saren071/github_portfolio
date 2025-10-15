"""
This is the launcher for all of my projects!!
"""

import json
import os
import platform
import subprocess
from collections import defaultdict

from constants import PROJECTS_DIRECTORY
from utils.logger import Logger


class Launcher:

    """
    This class handles the launcher itself.
    This will look for projects dynamically, and sort them alphabetically,
    along with categorizing them by hardcoded categories in a constants file.
    """

    def __init__(self):
        """
        This method initializes the launcher.
        """
        self.logger = Logger()
        self.logger.get_logger("launcher")
        self.projects = {}

    def add_project(self):
        """
        This method adds a project to the launcher.
        """
        # Check if the project directory exists
        if not os.path.exists(PROJECTS_DIRECTORY):
            self.logger.error("Project directory does not exist", "launcher")
            return

        # Check for the project name via the folder,
        # and then check for a main.py file IN the project,
        # along with an OPTIONAL details.json file

        for dir in os.listdir(PROJECTS_DIRECTORY):
            if os.path.isdir(os.path.join(PROJECTS_DIRECTORY, dir)):
                if os.path.exists(os.path.join(PROJECTS_DIRECTORY, dir, "main.py")):
                    self.logger.info(f"Adding project: {dir}", "launcher")

                    # Load details.json if it exists
                    details_path = os.path.join(PROJECTS_DIRECTORY, dir, "details.json")
                    details_data = {}
                    if os.path.exists(details_path):
                        try:
                            with open(details_path) as f:
                                details_data = json.load(f)
                        except json.JSONDecodeError as e:
                            self.logger.error(f"Invalid JSON in {details_path}: {e}", "launcher")

                    self.projects[dir] = {
                        "name": dir,
                        "main.py": os.path.join(PROJECTS_DIRECTORY, dir, "main.py"),
                        "details": details_data
                    }
                else:
                    self.logger.error(f"Project {dir} does not have a main.py file, this is required!", "launcher")

    def format_project_name(self, project_name):
        """
        Format project name to title case with spaces instead of underscores.
        """
        return project_name.replace('_', ' ').title()

    def get_projects_by_category(self):
        """
        Group projects by category and sort both categories and projects within categories.
        Returns a dict of {category: [sorted_project_list]} and a list of all projects in order.
        """
        # Group projects by category
        category_groups = defaultdict(list)

        for project_name in self.projects:
            details = self.projects[project_name]["details"]
            category = details.get('project_category', 'Other') if details else 'Other'
            category_groups[category].append(project_name)

        # Sort projects within each category alphabetically
        for category in category_groups:
            category_groups[category].sort()

        # Sort categories alphabetically
        sorted_categories = sorted(category_groups.keys())

        # Create ordered list of all projects for numbered selection
        ordered_projects = []
        for category in sorted_categories:
            ordered_projects.extend(category_groups[category])

        return category_groups, ordered_projects

    def display_project_details(self, project):
        """
        This method displays project details in a nice format.
        """
        details = self.projects[project]["details"]
        if not details:
            print(f"No details available for {project}")
            return

        print(f"\n{'=' * 50}")
        print(f"Project: {self.format_project_name(project)}")
        print(f"{'=' * 50}")

        # Display each detail on its own line
        for key, value in details.items():
            # Convert snake_case to Title Case for display
            display_key = key.replace('_', ' ').title()
            print(f"{display_key}: {value}")

        print(f"{'=' * 50}\n")

    def run_project(self, project):
        """
        This method runs a project.
        """
        # Display project details before launching
        self.display_project_details(project)

        # Ask for confirmation
        confirm = input("Launch this project? (y/n): ").lower().strip()
        if confirm != 'y':
            print("Launch cancelled.")
            return

        self.logger.info(f"Launching project: {project}", "launcher")

        python_version = platform.python_version().split(".")[0]
        if platform.system() == "Windows":
            subprocess.run([f"python{python_version}", self.projects[project]["main.py"]])
        elif platform.system() == "Linux":
            subprocess.run([f"python{python_version}", self.projects[project]["main.py"]])
        elif platform.system() == "Darwin":
            subprocess.run([f"python{python_version}", self.projects[project]["main.py"]])
        else:
            self.logger.error(f"Unsupported operating system: {platform.system()}", "launcher")
            return

    def main(self):
        """
        This method is the main method for the launcher.
        """
        self.logger.info("Starting launcher", "launcher")
        self.add_project()

        # Get projects grouped by category
        category_groups, ordered_projects = self.get_projects_by_category()

        print("Welcome to the Git Portfolio Launcher!")
        print("This is a collection of mini-programs designed to run through the launcher.py in the root.")
        print("Select a project by number or name to view details and launch.")

        while True:
            print("\nAvailable projects:")

            # Display projects grouped by category with numbers
            project_number = 1
            for category in sorted(category_groups.keys()):
                print(f"\n{category}:")
                for project in category_groups[category]:
                    formatted_name = self.format_project_name(project)
                    print(f"  {project_number}. {formatted_name}")
                    project_number += 1

            print("\nEnter the project number or name (or type 'q' to quit): ")
            user_input = input().strip()

            if user_input.lower() == "q":
                break

            # Try to parse as number first
            selected_project = None
            try:
                project_index = int(user_input) - 1  # Convert to 0-based index
                if 0 <= project_index < len(ordered_projects):
                    selected_project = ordered_projects[project_index]
                else:
                    print(f"Invalid project number. Please enter 1-{len(ordered_projects)}.")
                    continue
            except ValueError:
                # Not a number, treat as project name
                if user_input in self.projects:
                    selected_project = user_input
                else:
                    print(f"Project '{user_input}' not found.")
                    continue

            if selected_project:
                self.run_project(selected_project)

        self.logger.info("Launcher finished", "launcher")


if __name__ == "__main__":
    launcher = Launcher()
    launcher.main()
