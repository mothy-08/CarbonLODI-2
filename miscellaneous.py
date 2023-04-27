from abc import ABC, abstractmethod

class ErrorHandler(ABC):

    @abstractmethod
    def get_valid_option(self, prompt: str, valid_options: list) -> str:
        pass

    @abstractmethod
    def get_float(self, prompt: str) -> float:
        pass

    @abstractmethod
    def get_int(self, prompt: str) -> int:
        pass


class CarbonCalculator(ABC):

    @abstractmethod
    def calculate_housing_emissions(self):
        pass

    @abstractmethod
    def calculate_transportation_emissions(self):
        pass

    @abstractmethod
    def calculate_food_emissions(self):
        pass

    @abstractmethod
    def calculate_all(self, current_user):
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
