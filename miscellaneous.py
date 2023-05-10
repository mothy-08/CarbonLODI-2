from abstracts import ErrorHandlerABC
from abstracts import CarbonCalculatorABC
from abstracts import AccountManagerABC
from prettytable import PrettyTable
import os
import datetime


class Constants:
    logo = '''
   ______           __                   __    ____  ____  ____
  / ____/___ ______/ /_  ____  ____     / /   / __ \/ __ \/  _/
 / /   / __ `/ ___/ __ \/ __ \/ __ \   / /   / / / / / / // /  
/ /___/ /_/ / /  / /_/ / /_/ / / / /  / /___/ /_/ / /_/ // /   
\____/\__,_/_/  /_.___/\____/_/ /_/  /_____/\____/_____/___/   

                                                               '''

    main_menu = '''
                         Main Menu

                        1 - Register
                        2 - Login
                        0 - Exit
Response: '''


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

    def calculate_housing_emissions(self):  # Ask user for housing information

        house_size_sq_m = super().get_float("Size of your house (square meters): ")
        occupants = super().get_int("Number of occupants in your house: ")
        electricity_use = super().get_float("Electric consumption per month (kWH): ")
        cooking_fuel = super().get_int("Enter the type of cooking fuel (1-LPG, 2-Electric, 3-Bio): ")

        lpg_emissions = 0
        if cooking_fuel == 1:
            lpg_use = super().get_float("Estimate the number of days your 11 kg LPG lasts: ")
            lpg_emissions = (
                                    35 / lpg_use) * 30  # 35 CO2e = (30 per LPG cylinder) + (5 average CO2e of stove per Cylinder)

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
        date = datetime.datetime.now()
        filename = f"user-{current_user}.txt"  # names '.txt' files for each user
        total_emissions = self.calculate_housing_emissions() + self.calculate_transportation_emissions() + self.calculate_food_emissions()
        print(f"Today's total carbon emission is {total_emissions} grams")
        input('Press any key to continue...')
        with open(filename, 'a') as file:
            file.write(f"{date.strftime('%Y-%m-%d')} : {round(total_emissions, 2)}\n")


class AccountManager(AccountManagerABC, CarbonCalculator):
    """
    This is a Class for Account Managing.
    Functions:
        encrypt_password(password): (Private) Encrypts a password using a secret key.
        register(): Prompts user for creating account info and stores it in 'users' dict and 'accounts.txt' file.
        load_users(): Loads user account information from the 'accounts.txt' file into the 'users' dict.
        login(): Prompts the user to login and checks if it matches a stored user account in the 'user' dict.
    """

    def __init__(self):
        self.current_user = None
        self.record = {}
        self.users = {}
        if os.path.exists("accounts.txt"):
            self.load_users()

    @staticmethod
    def __encrypt_password(password):  # (Private) Encrypts a password using a secret key.

        __secret_key = "MathintheModernWorld"
        encrypted_password = ""
        for i, char in enumerate(password):  # Shifts each character by certain amount depending on the '__secret_key'
            shift = ord(__secret_key[i % len(__secret_key)]) - ord('a')
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_password += shifted_char
        return encrypted_password

    def register(self):  # Prompts user for creating account info and stores it in 'users' dict and 'accounts.txt' file.

        while True:
            username = input("Enter your username: ")
            if username in self.users:
                print("Username already exists. Please choose a different username.")
            else:
                break
        password = input("Enter a password: ")
        encrypted_password = self.__encrypt_password(password)
        self.users[username] = {'password': encrypted_password}
        with open("accounts.txt", 'a') as file:  # Appends every account into 'accounts.txt'
            file.write(f"{username}:{encrypted_password}\n")
        print("Registration successful.")
        return username

    def load_users(self):  # Loads user account information from the 'accounts.txt' file into the 'users' dict.
        with open("accounts.txt", 'r') as file:
            for line in file:
                username, encrypted_password = line.strip().split(':')
                self.users[username] = {'password': encrypted_password}

    def login(self):  # Prompts the user to login and checks if it matches a stored user account in the 'user' dict.
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        encrypted_password = self.__encrypt_password(password)
        if username in self.users and self.users[username]['password'] == encrypted_password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Invalid username or password.")

    def generate_table(self, current_user):
        user_data = {}
        with open(f'user-{current_user}.txt', 'r') as file:
            for line in file:
                date, emissions = line.strip().split(' : ')
                user_data[date] = emissions

        max_date_len = max(len(date) for date in user_data.keys())
        max_emissions_len = max(len(emissions) for emissions in user_data.values())

        table = []
        table.append(['Date'.ljust(max_date_len), 'Total Emissions (grams)'.ljust(max_emissions_len)])
        for date, emissions in user_data.items():
            table.append([date.ljust(max_date_len), emissions.ljust(max_emissions_len)])

        for row in table:
            print(row[0], '|', row[1])

    def show_home(self, current_user):
        self.current_user = current_user
        main_menu = '''
                            Menu

                        1 - Calculate Emission
                        2 - Track
                        0 - Log out
Response: '''
        os.system('cls')
        print(Constants.logo)
        choice = super().get_valid_option(main_menu, ['1', '2', '0'])
        if choice == '1':
            super(AccountManager, self).calculate_all(self.current_user)
            input("Press Enter to continue...")
        elif choice == '2':
            self.generate_table(current_user)
        else:
            pass
