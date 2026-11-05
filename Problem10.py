class Weather:
    def _init_(self, temp):
        self.temp= temp

    def display(self):
        print("Temperature is ", self.temp)

    def weather_condition(self):
        if(self.temp <= 20) :
            print("Cold")
        elif(self.temp > 20 and self.temp<= 25) :
            print ("Windy")
        elif(self.temp > 25 and self.temp<= 30) :
            print ("Cloudy")
        elif(self.temp> 30 and self.temp <= 35) :
            print ("Suitable")
        elif(self.temp> 35 and self.temp<= 40) :
            print ("Hot")
        else :
            print("Extremely hot")

user_input= int(input("Enter temperature: "))
tempt= Weather(user_input)
tempt.display()
tempt.weather_condition()