"""
A manufacturing company needs a program that will help its employees pack manufactured items
into boxes for shipping. Write a Python progra that asks the user for two integers:
1. the number of manufactured items
2. the number of items that the user will pack per box
Your program must compute and print the number of boxes necessary to hold the items..
This must be whole number. Note that the last box may  be packed with fewer items than the other boxes.
"""
import math
#Number of manufactured items
num_items = int(input("Enter the number of items: "))

#Number of items per box
items_per_box = int(input("Enter number of items per box: "))

#Number of boxes
num_box = math.ceil(num_items / items_per_box)

print(f"For {num_items} items, packing {items_per_box} items in each box, you will need {num_box}.")