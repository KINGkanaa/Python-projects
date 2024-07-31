import random
from colorama import Fore 

red = Fore.RED
black = Fore.BLACK
green = Fore. GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

def tempertureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = ( user_input - 32) * 5/9 

    if(user_input >=90):
        print("Fahrenheit: ", red, user_input, black)
        print("Celsius: " ,red, "{0:10.1f}".format(FAHRENHEIT_TO_CELSIUS) ,black)
    elif(user_input >=75) & (user_input <=89):
        print("Fahrenheit :",yellow, user_input, black)
        print("Celsius: " ,yellow, "{0:10.1f}".format(FAHRENHEIT_TO_CELSIUS),black)
    elif(user_input >=64) & (user_input <=74):
        print("Fahrenheit :", green, user_input,black)
        print("Celsius:" , green, "{0:10.1f}".format(FAHRENHEIT_TO_CELSIUS),black)
    else: 
        print("Fahrenheit :", blue, user_input,black)
        print("Celsius :", blue,"{0:10.1f}".format(FAHRENHEIT_TO_CELSIUS),black)

user= float(input("Enter a temperature in Fahrenheit to convert to Celsius: ") )

for x in range(5): 
   tempertureConverter(user)
   user=float(input("Enter a temperature in Fahrenheit to convert to Celsius: ") )
