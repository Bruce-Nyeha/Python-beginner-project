"""
1. Have the user enter a tir width in mm
2. Have the user enter the aspect ratio
3. Have the user enter the diameter of the wheel in inches
4. Calculate and display the tire's volume
5. Log the information in a text file
5.1 current date (Do NOT innclude time)
5.2 width of the tire
5.3 aspect of the ratio 
5.4 diameter of the wheel
5.5 volume of the tire (rounded to two decimal places).
"""
import math
from datetime import datetime
print("Today we are going to look at thee volume calculation of a tire")

current_date = datetime.now().date()

#The width of the tire in mm
tire_width = int(input("Enter a tire width in mm (ex 205): "))

#The ratio of the tire
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))

#The diameter of the wheel 
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#Volume of the tire
volume = (math.pi * tire_width**2 * ratio * (tire_width * ratio + 2540 * diameter)) / 10000000000

volume = round(volume, 2)
#User view
print(f"The approximate volume is {volume} liters")

#Current date
print(f"Current date: {current_date}")

#Write and save the details in a file called volume.text
with open("volumes.txt","at") as file:
    file.write(f"{current_date}, {tire_width}, {ratio}, {diameter}, {volume}\n")
    print("Data has been saved successfully!")


"""
1. Add a set of if, elif, else statements in your program that use the tire width,
tire aspect ratio, and wheel diameter that the user enters to find a price then print the prince

2. After your  program prints the tire volume to the terminal window, your program should ask the user if she wants
to buy tires with the dimensions that she entered. if the user answers "yes", your program should ask for her 
phone number and store her phone number in the volumes.text file
"""
#using condtional statements to find the prices
if tire_width ==205 and ratio==60 and diameter ==15:
    price = 150.99

elif tire_width ==210 and ratio==70 and diameter==30:
    price = 170.99

elif tire_width==220 and ratio== 80 and diameter == 50:
    price = 180.99

else:
    price = 189.99

print(f"The estimated price for these tires  is ${price: .2f} each.") 

#Ask if user wants to buy tires
buy_tires = input("Do you want to purchase with these dimensions? (Yes/No) ").lower()

phone_number = "Not Yet"

if buy_tires == "yes":
    phone_number = input("Please input your phone number: ")
    print("Thank you! We'll contact you soon.")

#Now we store the whole data back to the volume.txt file 
with open("volumes.txt", "at") as file:
    file.write(f"Date: {current_date}, Tire Width: {tire_width}, ratio: {ratio},diameter: {diameter}, volume: {volume}, price: ${price}, phone number: {phone_number}\n")

print("Data stored successfully!")