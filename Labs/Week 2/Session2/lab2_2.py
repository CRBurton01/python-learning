# lab2_2.py
# Week 2 Session 2 Lab
# Cody Burton
# 8/28/2025

print("=" * 50)
print("WEEK 2 SESSION 2 LAB")
print("=" * 50)

#======================PROBLEM 1 : Age Calculator==========================

print("\n--- Problem 1: Age Calculator ---")
# TODO: Get birth year from user and convert to integer
birth_year = int(input("Enter your birth year: "))
# TODO: Calculate age (assume current year is 2024)
age = 2024 - birth_year
# TODO: Print "You are ___ years old in 2024."
print(f"You are {age} years old in 2024.")
# Test with: 2000 → Should output: You are 24 years old in 2024.

#======================PROBLEM 2 : Temperature Converter==========================

print("\n--- Problem 2: Temperature Converter ---")
# TODO: Get Celsius temperature and convert to float
celcius = float(input("Enter temperature in Celsius: "))
# TODO: Calculate Fahrenheit
fahrenheit = (celcius * 9/5) + 32
# TODO: Print both temperatures with 1 decimal place
print(f"{celcius:.1f}°C = {fahrenheit:.1f}°F")
# Test with: 25 → Should output: 25.0°C = 77.0°F

#======================PROBLEM 3 : Rectangle Measeurements==========================
print("\n--- Problem 3: Rectangle Measurements ---")
# TODO: Get length and width as floats
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
# TODO: Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)
# TODO: Display with 2 decimal places
print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")
# Test with: length=5.5, width=3.2
# Should output: Area: 17.60, Perimeter: 17.40

#======================PROBLEM 4 : Bill Calculator==========================
print("\n--- Problem 4: Bill Calculator ---")
# TODO: Get meal cost and tip percentage
meal_cost = float(input("Enter meal cost: "))
tip_percentage = float(input("Enter tip percentage (e.g., 20 for 20%): "))
# TODO: Calculate tip amount and total
tip_amount = meal_cost * (tip_percentage / 100)
total_cost = meal_cost + tip_amount
# TODO: Display all amounts with 2 decimal places
print(f"Meal: ${meal_cost:.2f}, Tip: ${tip_amount:.2f}, Total: ${total_cost:.2f}")
# Test with: meal=$50, tip=20%
# Should output: Meal: $50.00, Tip: $10.00, Total: $60.00

#======================PROBLEM 5 : Student Info Display==========================
print("\n--- Problem 5: Student Info Display ---")
# TODO: Get name, age, major from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
major = input("Enter your major: ")
# TODO: Display with:
# 1. Default spacing
print(name, age, major)
# 2. Comma separation (use sep=", ")
print(name, age, major, sep=", ")
# 3. Pipe separation (use sep=" | ")
print(name, age, major, sep=" | ")
# Test with: Alice, 20, Computer Science
# Should show three different formats

#======================PROBLEM 6 : Progress Indicator==========================
print("\n--- Problem 6: Progress Indicator ---")
# TODO: Print "Processing" without newline
print("Processing", end="")
# TODO: Add 5 dots without newlines (use end="")
for _ in range(5):
    print(".", end="")
# TODO: Print " Complete!"
print(" Complete!")
# Should output: Processing..... Complete!

#======================PROBLEM 7 : Data Table Header==========================print("\n--- Problem 7: Data Table Header ---")
print("\n--- Problem 7: Data Table Header ---")
# TODO: Get student name, score, grade
student_name = input("Enter student name: ")
student_score = float(input("Enter student score: "))
student_grade = input("Enter student grade: ")
# TODO: Print a line of 40 equal signs
print("=" * 40)
# TODO: Print "Name", "Score", "Grade" with tab separation
print("Name\tScore\tGrade")
# TODO: Print another line of 40 equal signs
print("=" * 40)
# TODO: Display one student's data with tabs
print(f"{student_name}\t{student_score:.2f}\t{student_grade}")
# Should create a simple table structure

#======================PROBLEM 8 : Message Box==========================
print("\n--- Problem 8: Message Box ---")
# TODO: Get a short message from user
message = input("Enter a short message: ")
# TODO: Print top border (use "+" and "-" × 30)
print("+" + "-" * 30 + "+")
# TODO: Print message with "| " before and after
print (f"| {message:<28} |")
# TODO: Print bottom border
print("+" + "-" * 30 + "+")
# Test with: "Hello World"
# Should create a box around the message

#======================END OF LAB==========================

#======================BONUS PROBLEMS==========================

#======================PROBLEM 9 : Price Display==========================
print("\n--- Problem 9: Price Display ---")
# TODO: Get item name and price
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
# TODO: Display as: "Item: ________ Price: $__.__ "
print(f"Item: {item_name:<10} Price: ${item_price:>6.2f}")
# TODO: Use f-string to right-align price in 8 characters

# Test with: Apple, 1.5
# Should output: Apple $ 1.50