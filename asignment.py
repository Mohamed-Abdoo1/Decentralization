
class ElectricVehicle: # Define a class for electric vehicles

    def _init_(self, battery_capacity): # Constructor for ElectricVehicle class (that has one parameter)
        
        self.battery_capacity = battery_capacity # Initialize the battery_capacity attribute

    def display_battery_info(self): # Method to display the battery information
                print(f"Battery Capacity: {self.battery_capacity} kWh") # Print the battery capacity of the electric vehicle




class GasolineVehicle: # Define a class for gasoline vehicles
    
    def _init_(self, fuel_capacity): # Constructor for GasolineVehicle class 
        
        self.fuel_capacity = fuel_capacity  # Initialize the fuel_capacity attribute

    
    def display_fuel_info(self): # Method to display the fuel information
        
        print(f"Fuel Capacity: {self.fuel_capacity} liters") # Print the fuel capacity of the gasoline vehicle



class HybridCar(ElectricVehicle, GasolineVehicle): # Define a class for hybrid cars that inherits from both ElectricVehicle and GasolineVehicle
    # Constructor for HybridCar class (note the typo in __init__)
    def _init_(self, battery_capacity, fuel_capacity, model):
        # Initialize the ElectricVehicle part of HybridCar
        ElectricVehicle._init_(self, battery_capacity)
        # Initialize the GasolineVehicle part of HybridCar
        GasolineVehicle._init_(self, fuel_capacity)
        # Initialize the model attribute specific to HybridCar
        self.model = model

    # Method to display information specific to the hybrid car
    def display_hybrid_info(self):
        # Print the model of the hybrid car
        print(f"Model: {self.model}")
        # Call the method to display battery information
        self.display_battery_info()
        # Call the method to display fuel information
        self.display_fuel_info()


# Create an instance of HybridCar with specified attributes
hybrid_car = HybridCar(15, 50, "Toyota Prius")

# Display information about the hybrid car
hybrid_car.display_hybrid_info()

"""The code is designed to create a hybrid vehicle class that combines properties of both 
electric and gasoline vehicles and can display information about both types of power sources. """
