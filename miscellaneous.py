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

class CarbonCalculator(CarbonCalculatorABC, ErrorHandler):

    def __init__(self, current_user):
        self.filename = f"user-{current_user}.txt"  # names '.txt' files for each user

    def calculate_housing_emissions(self):  # Ask user for housing information

        house_size_sq_m = self.get_float("Size of your house (square meters): ")
        occupants = self.get_int("Number of occupants in your house: ")
        electricity_use = self.get_float("Electric consumption per month (kWH): ")
        cooking_fuel = self.get_int("Enter the type of cooking fuel (1-LPG, 2-Electric, 3-Bio): ")

        lpg_emissions = 0
        if cooking_fuel == 1:
            lpg_use = self.get_float("Estimate the number of days your 11 kg LPG lasts: ")
            lpg_emissions = (35 / lpg_use) * 30  # 35 CO2e = (30 per LPG cylinder) + (5 average CO2e of stove per Cylinder)

        #  Formulas per month
        house_size_sq_ft = house_size_sq_m * 10.764  # 1 sq m = 10.764 sq ft
        electricity_emissions = electricity_use * 0.5  # 0.5 kg CO2e per kWH

        # Convert to grams per day
        return ((electricity_emissions + lpg_emissions) / occupants / house_size_sq_ft) * 1000 / 30
