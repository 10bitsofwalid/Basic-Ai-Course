# ==========================================
# Problem 10: Weather Condition Classifier (OOP)
# Description: Defines a Weather class to encapsulate temperature data
#              and classify environmental conditions into descriptive categories.
# ==========================================

# Step 1: Define the Weather class
class Weather:
    # Fixed bug: Changed '_init_' to standard '__init__' constructor
    def __init__(self, temp):
        """Initialize Weather object with a temperature value."""
        self.temp = temp

    # Step 2: Method to display the current recorded temperature
    def display(self):
        """Print current temperature."""
        print(f"Temperature is {self.temp}°C")

    # Step 3: Method to evaluate and print the weather condition
    def weather_condition(self):
        """Classify condition based on temperature brackets."""
        if self.temp <= 20:
            print("Weather Condition: Cold")
        elif 20 < self.temp <= 25:
            print("Weather Condition: Windy")
        elif 25 < self.temp <= 30:
            print("Weather Condition: Cloudy")
        elif 30 < self.temp <= 35:
            print("Weather Condition: Suitable")
        elif 35 < self.temp <= 40:
            print("Weather Condition: Hot")
        else:
            print("Weather Condition: Extremely hot")


# Step 4: Prompt the user to enter temperature
user_input = int(input("Enter temperature: "))

# Step 5: Instantiate Weather object with user's input
tempt = Weather(user_input)

# Step 6: Invoke methods to display temperature and classified weather
tempt.display()
tempt.weather_condition()
