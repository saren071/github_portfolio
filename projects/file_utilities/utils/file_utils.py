"""
This will handle all file operations for the file organizer.
We will be using Python 3.14 free-threading capabilities to handle file operations,
so we can concurrently handle file operations.
"""


import os


class FileUtils:
    """
    This class will handle the file utilities.
    """
    def __init__(self):
        """
        This method initializes the file utilities.
        """
        pass

    def get_file_type(self, file_path):
        """
        This method will get the file type of a file.
        """
        return os.path.splitext(file_path)[1]

    def get_file_size(self, file_path):
        """
        This method will get the size of a file.
        """
        return os.path.getsize(file_path)

    def get_file_date(self, file_path):
        """
        This method will get the date of a file.
        """
        return os.path.getmtime(file_path)
