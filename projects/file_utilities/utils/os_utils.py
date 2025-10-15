"""
This file will simply detect which operating system the user is on
and return the appropriate operations for the operating system.
"""

import platform


class OSUtils:
    """
    This class will handle the operating system utilities.
    """
    def __init__(self):
        """
        This method initializes the operating system utilities.
        """
        pass

    def get_operating_system(self):
        """
        This method will get the operating system.
        """
        return platform.system()

    def get_operating_system_version(self):
        """
        This method will get the operating system version.
        """
        return platform.version()

    def get_operating_system_architecture(self):
        """
        This method will get the operating system architecture.
        """
        return platform.machine()

    def get_operating_system_platform(self):
        """
        This method will get the operating system platform.
        """
        return platform.platform()

    def get_operating_system_processor(self):
        """
        This method will get the operating system processor.
        """
        return platform.processor()

    def get_operating_system_machine(self):
        """
        This method will get the operating system machine.
        """
        return platform.machine()
