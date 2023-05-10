from abc import ABC, abstractmethod


class ErrorHandlerABC(ABC):

    @abstractmethod
    def get_valid_option(self, prompt, valid_options):
        pass

    @abstractmethod
    def get_float(self, prompt):
        pass

    @abstractmethod
    def get_int(self, prompt):
        pass


class CarbonCalculatorABC(ABC):

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

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def load_users(self):
        pass

    @abstractmethod
    def login(self):
        pass

    @staticmethod
    @abstractmethod
    def file_to_dict(current_user):
        pass

    @staticmethod
    @abstractmethod
    def generate_table(data_dict):
        pass
