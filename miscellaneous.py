from abc import ABC, abstractmethod

class ErrorHandler(ABC):
    """
    Abstract Base Class for Error Handling.
    """

    @abstractmethod
    def get_valid_option(self, prompt: str, valid_options: list) -> str:
        """
        Checks if the user input is valid.
        """
        pass

    @abstractmethod
    def get_float(self, prompt: str) -> float:
        """
        Checks if the user input is a float that is greater than 0.
        """
        pass

    @abstractmethod
    def get_int(self, prompt: str) -> int:
        """
        Checks if the user input is a integer that is greater than 0.
        """
        pass


class CarbonCalculator(ABC):
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
