from abstracts import ErrorHandlerABC
from abstracts import CarbonCalculatorABC
from abstracts import AccountManagerABC
import os

class ErrorHandler(ErrorHandlerABC):
    def get_valid_option(self, prompt, valid_options):
        while True:
            option = input(prompt)
            if option in valid_options:
                return option
            else:
                print(f"Invalid input.")

    def get_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def get_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid value.")

