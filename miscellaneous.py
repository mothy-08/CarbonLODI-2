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

        house_size_sq_m = super().get_float("Size of your house (square meters): ")
        occupants = super().get_int("Number of occupants in your house: ")
        electricity_use = super().get_float("Electric consumption per month (kWH): ")
        cooking_fuel = super().get_int("Enter the type of cooking fuel (1-LPG, 2-Electric, 3-Bio): ")

        lpg_emissions = 0
        if cooking_fuel == 1:
            lpg_use = super().get_float("Estimate the number of days your 11 kg LPG lasts: ")
            lpg_emissions = (35 / lpg_use) * 30  # 35 CO2e = (30 per LPG cylinder) + (5 average CO2e of stove per Cylinder)

        #  Formulas per month
        house_size_sq_ft = house_size_sq_m * 10.764  # 1 sq m = 10.764 sq ft
        electricity_emissions = electricity_use * 0.5  # 0.5 kg CO2e per kWH

        # Convert to grams per day
        return ((electricity_emissions + lpg_emissions) / occupants / house_size_sq_ft) * 1000 / 30
    
    def calculate_transportation_emissions(self):
        transportation_type = self.get_valid_option('''
            Your form of transportation 
                0 - Walking
                1 - Private Vehicle
                2 - Public Vehicle

Response: ''', ['0', '1', '2'])

        if transportation_type == '0':
            transportation_co2e = 0  # No emissions for walking
        elif transportation_type == '1':
            passengers = super().get_int("Number of people in the vehicle: ")
            distance = super().get_float("Distance of your transportation (km): ")
            fuel_efficiency = super().get_float(
                "What is the fuel efficiency of the vehicle (in km/L)? ")
            fuel_type = input("What type of fuel does the vehicle use? (1 - Gasoline / 2 - Diesel) ")
            emissions_factor = 2352.7 if fuel_type == '1' else 2639.4 if fuel_type == '2' else 0
            transportation_co2e = (emissions_factor * distance / fuel_efficiency) / passengers
        elif transportation_type == '2':
            distance = super().get_float("Distance of your transportation (km): ")
            transportation_co2e = 90 * distance  # 90 g CO2e/km/passenger on average for public transportation
        else:
            print("Sorry, we didn't understand your transportation type.")
            transportation_co2e = 0

        return transportation_co2e
    
    def calculate_food_emissions(self):
        emissions_dict = {}
        with open("food.txt") as f:
            for line in f:
                food, emissions = line.strip().split(":")
                emissions_dict[food] = float(emissions)
        food_items = []
        while True:
            food_item = input("Enter a food item you ate today (or 'done' if finished): ")
            if food_item == 'done':
                break
            else:
                food_items.append(food_item)

        food_co2e = 0
        for food_item in food_items:
            if food_item in emissions_dict:
                servings = super().get_float(f"Your servings of {food_item} (grams) ")
                food_co2e += (servings * emissions_dict[food_item])
            else:
                print(f"Sorry, we don't have emissions data for {food_item}. Skipping...")
        return food_co2e

    def calculate_all(self, current_user):
        total_emissions = self.calculate_housing_emissions() + self.calculate_transportation_emissions() + self.calculate_food_emissions()
        with open(self.filename, 'a') as file:
            file.write(total_emissions)
