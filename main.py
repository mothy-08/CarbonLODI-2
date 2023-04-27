
class Transportation:
    def __init__(self, fuel_type, distance, vehicle_type, transport_type):
        self.fuel_type = fuel_type
        self.distance = distance
        self.vehicle_type = vehicle_type
        self.transport_type = transport_type

    def calculate_emissions(self):
        emissions = 0
        if self.transport_type == 'car':
            if self.fuel_type == 'gasoline':
                if self.vehicle_type == 'sedan':
                    emissions = self.distance * 0.2  # 0.2 kg CO2 per km for a gasoline sedan
                elif self.vehicle_type == 'suv':
                    emissions = self.distance * 0.3  # 0.3 kg CO2 per km for a gasoline SUV
            elif self.fuel_type == 'diesel':
                if self.vehicle_type == 'sedan':
                    emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a diesel sedan
                elif self.vehicle_type == 'suv':
                    emissions = self.distance * 0.25  # 0.25 kg CO2 per km for a diesel SUV
        elif self.transport_type == 'train':
            if self.fuel_type == 'electricity':
                emissions = self.distance * 0.05  # 0.05 kg CO2 per km for an electric train
            elif self.fuel_type == 'diesel':
                emissions = self.distance * 0.1  # 0.1 kg CO2 per km for a diesel train
        elif self.transport_type == 'bus':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.2  # 0.2 kg CO2 per km for a gasoline bus
            elif self.fuel_type == 'diesel':
                emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a diesel bus
        elif self.transport_type == 'motorcycle':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.15  # 0.15 kg CO2 per km for a gasoline motorcycle
            elif self.fuel_type == 'electricity':
                emissions = self.distance * 0.05  # 0.05 kg CO2 per km for an electric motorcycle
        elif self.transport_type == 'tricycle':
            if self.fuel_type == 'gasoline':
                emissions = self.distance * 0.1  # 0.1 kg CO2 per km for a gasoline tricycle
            elif self.fuel_type == 'electricity':
                emissions = self.distance * 0.03  # 0.03 kg CO2 per km for an electric tricycle
        elif self.transport_type == 'walking' or 'cycling':
            emissions = self.distance * 0.00
        return emissions

class House:
    def __init__(self, square_footage, num_residents, energy_source, num_vehicles, location):
        self.square_footage = square_footage  # in square feet
        self.num_residents = num_residents
        self.energy_source = energy_source  # "electricity", "natural_gas", or "oil"
        self.num_vehicles = num_vehicles
        self.location = location  # "urban", "suburban", or "rural"

    def calculate_emissions(self):
        electricity_emissions = self.square_footage * 0.15  # 0.15 lbs CO2 per sq ft per month
        natural_gas_emissions = self.square_footage * 0.12  # 0.12 lbs CO2 per sq ft per month
        oil_emissions = self.square_footage * 0.18  # 0.18 lbs CO2 per sq ft per month

        if self.energy_source == "electricity":
            total_emissions = electricity_emissions
        elif self.energy_source == "natural_gas":
            total_emissions = natural_gas_emissions
        elif self.energy_source == "oil":
            total_emissions = oil_emissions
        else:
            raise ValueError("Invalid energy source")

        total_emissions += self.num_residents * 44  # 44 lbs CO2 per person per month

        if self.location == "urban":
            total_emissions += self.num_vehicles * 24  # 24 lbs CO2 per vehicle per month
        elif self.location == "suburban":
            total_emissions += self.num_vehicles * 15  # 15 lbs CO2 per vehicle per month
        elif self.location == "rural":
            total_emissions += self.num_vehicles * 10  # 10 lbs CO2 per vehicle per month
        else:
            raise ValueError("Invalid location")

        return total_emissions


class Diet:
    def __init__(self, meat_consumption, dairy_consumption, grain_consumption, fruit_veg_consumption,
                 seafood_consumption, meat_source, dairy_source, grain_source, fruit_veg_source, seafood_source):
        self.meat_consumption = meat_consumption
        self.dairy_consumption = dairy_consumption
        self.grain_consumption = grain_consumption
        self.fruit_veg_consumption = fruit_veg_consumption
        self.seafood_consumption = seafood_consumption
        self.meat_source = meat_source
        self.dairy_source = dairy_source
        self.grain_source = grain_source
        self.fruit_veg_source = fruit_veg_source
        self.seafood_source = seafood_source

    def calculate_carbon_footprint(self):
        meat_emissions = self.meat_consumption * 6.61  # in kg CO2e per kg of meat
        dairy_emissions = self.dairy_consumption * 2.44  # in kg CO2e per kg of dairy
        grain_emissions = self.grain_consumption * 0.65  # in kg CO2e per kg of grains
        fruit_veg_emissions = self.fruit_veg_consumption * 0.29  # in kg CO2e per kg of fruits and vegetables
        seafood_emissions = self.seafood_consumption * 3.0  # in kg CO2e per kg of seafood

        # emissions from food source
        meat_source_emissions = 0
        dairy_source_emissions = 0
        grain_source_emissions = 0
        fruit_veg_source_emissions = 0
        seafood_source_emissions = 0

        if self.meat_source == "beef":
            meat_source_emissions = self.meat_consumption * 0.06  # in kg CO2e per g of beef
        elif self.meat_source == "pork":
            meat_source_emissions = self.meat_consumption * 0.008  # in kg CO2e per g of pork
        elif self.meat_source == "chicken":
            meat_source_emissions = self.meat_consumption * 0.006  # in kg CO2e per g of chicken

        if self.dairy_source == "cow":
            dairy_source_emissions = self.dairy_consumption * 0.0024  # in g CO2e per g of dairy from cows
        elif self.dairy_source == "goat":
            dairy_source_emissions = self.dairy_consumption * 0.00092  # in g CO2e per g of dairy from goats

        if self.grain_source == "imported":
            grain_source_emissions = self.grain_consumption * 0.0011  # in g CO2e per kg of imported grains
        elif self.grain_source == "local":
            grain_source_emissions = self.grain_consumption * 0.0003  # in g CO2e per kg of local grains

        if self.fruit_veg_source == "imported":
            fruit_veg_source_emissions = self.fruit_veg_consumption * 0.0011  # in kg CO2e per kg of imported fruits and vegetables
        elif self.fruit_veg_source == "local":
            fruit_veg_source_emissions = self.fruit_veg_consumption * 0.0003  # in kg CO2e per kg of local fruits and vegetables

        if self.seafood_source == "wild":
            seafood_source_emissions = self.seafood_consumption * 0.003  # in kg CO2e per kg of wild-caught seafood
        elif self.seafood_source == "farmed":
            seafood_source_emissions = self.seafood_consumption * 0.0015 # in kg CO2e per kg of farmed seafood

        total_emissions = meat_emissions + dairy_emissions + grain_emissions + fruit_veg_emissions + seafood_emissions + \
                      meat_source_emissions + dairy_source_emissions + grain_source_emissions + \
                      fruit_veg_source_emissions + seafood_source_emissions

        return total_emissions


def set_diet(self, meat_consumption, dairy_consumption, grain_consumption, fruit_veg_consumption, seafood_consumption,
             meat_source, dairy_source, grain_source, fruit_veg_source, seafood_source):
    self.meat_consumption = meat_consumption
    self.dairy_consumption = dairy_consumption
    self.grain_consumption = grain_consumption
    self.fruit_veg_consumption = fruit_veg_consumption
    self.seafood_consumption = seafood_consumption
    self.meat_source = meat_source
    self.dairy_source = dairy_source
    self.grain_source = grain_source
    self.fruit_veg_source = fruit_veg_source
    self.seafood_source = seafood_source


def get_diet(self):
    return self.meat_consumption, self.dairy_consumption, self.grain_consumption, self.fruit_veg_consumption, \
        self.seafood_consumption, self.meat_source, self.dairy_source, self.grain_source, \
        self.fruit_veg_source, self.seafood_source


# class Clothing:
#     def __init__(self, material, source, manufacturing_location, transportation_method, transportation_distance):
#         self.material = material
#         self.source = source
#         self.manufacturing_location = manufacturing_location
#         self.transportation_method = transportation_method
#         self.transportation_distance = transportation_distance
#
#     def calculate_carbon_emissions(self):
#         material_emissions = self.get_material_emissions()
#         manufacturing_emissions = self.get_manufacturing_emissions()
#         transportation_emissions = self.get_transportation_emissions()
#         total_emissions = material_emissions + manufacturing_emissions + transportation_emissions
#         return total_emissions
#
#     def get_material_emissions(self):
#         if self.material == "cotton":
#             return 4.4  # kgCO2eq/kg of cotton
#         elif self.material == "polyester":
#             return 7.4  # kgCO2eq/kg of polyester
#         elif self.material == "wool":
#             return 15.2  # kgCO2eq/kg of wool
#         elif self.material == "nylon":
#             return 5.5  # kgCO2eq/kg of nylon
#         else:
#             return 0
#
#     def get_manufacturing_emissions(self):
#         if self.manufacturing_location == "USA":
#             return 3.6  # kgCO2eq/kg for manufacturing in the USA
#         elif self.manufacturing_location == "China":
#             return 7.8  # kgCO2eq/kg for manufacturing in China
#         elif self.manufacturing_location == "India":
#             return 4.9  # kgCO2eq/kg for manufacturing in India
#         else:
#             return 0
#
#     def get_transportation_emissions(self):
#         if self.transportation_method == "truck":
#             if self.transportation_distance < 100:
#                 return 0.13  # kgCO2eq/kg-km for truck transportation < 100 km
#             elif self.transportation_distance < 500:
#                 return 0.08  # kgCO2eq/kg-km for truck transportation < 500 km
#             else:
#                 return 0.05  # kgCO2eq/kg-km for truck transportation >= 500 km
#         elif self.transportation_method == "ship":
#             if self.source == "domestic":
#                 return 0.01  # kgCO2eq/kg-km for domestic shipping
#             else:
#                 return 0.005  # kgCO2eq/kg-km for international shipping
#         elif self.transportation_method == "air":
#             return 0.57  # kgCO2eq/kg-km for air transportation
#         else:
#             return 0

#needs error handling



if __name__ == '__main__':
    main()
