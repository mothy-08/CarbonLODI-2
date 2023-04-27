from abc import ABC, abstractmethod

class ErrorHandlerABC(ABC):
    """
    Handles posible logical error by filtering user's input
    """
    @abstractmethod
    def get_valid_option(self, prompt, valid_options):
        """
        Gets a valid option from the user, given a prompt and a list of valid options.

        Args:
            prompt (str): The prompt to display to the user.
            valid_options (list of str): The list of valid options.

        Returns:
            str: The valid option entered by the user.
        """
        pass

    @abstractmethod
    def get_float(self, prompt):
        """
        Gets a valid float value from the user, given a prompt.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            float: The valid float value entered by the user.
        """
        pass

    @abstractmethod
    def get_int(self, prompt):
        """
        Gets a valid integer value from the user, given a prompt.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            int: The valid integer value entered by the user.
        """
        pass


class CarbonCalculatorABC(ABC):
    """
    Abstract Base Class for Calculating Carbon Footprint.
    """

    @abstractmethod
    def calculate_housing_emissions(self):
        """
        Prompts user to give housing info to covert it into co2e.
        """
        pass

    @abstractmethod
    def calculate_transportation_emissions(self):
        """
        Prompts user to give transportation info to covert it into co2e.
        """
        pass

    @abstractmethod
    def calculate_food_emissions(self):
        """
        Prompts user to give food info to covert it into co2e.
        """
        pass

    @abstractmethod
    def calculate_all(self, current_user):
        """
        Calculate the total co2e.
        """
        pass
    
class AccountManagerABC(ABC):
    """
    Abstract Base Class for Account Managing.
    """

    @abstractmethod
    def register(self):
        """
        Prompts user for creating account info and stores it in 'users' dict and 'accounts.txt' file.
        """
        pass

    @abstractmethod
    def load_users(self):
        """
        Loads user account information from the 'accounts.txt' file into the 'users' dict.
        """
        pass

    @abstractmethod
    def login(self):
        """
        Prompts the user to login and checks if it matches a stored user account in the 'user' dict.
        """
        pass

    @abstractmethod
    def show_home(self, current_user):
        """
        Shows the main menu of the account management system.
        """
        pass
