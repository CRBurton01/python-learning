#CS 1300 - Homework 2
# Name: Cody Burton
# Date: 9/8/2025
# Description: Variables, Input/Output, and Type Conversions

# Problem 1 - Personal Finance Calculator
print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)
monthly_income = float(input("Enter your monthly income: $"))
rent_expense = float(input("Enter your monthly rent expense: $"))
food_expense = float(input("Enter your monthly food expense: $"))
transport_expns = float(input("Enter your monthly transportation expense: $"))
other_expense = float(input("Enter your other monthly expenses: $"))

total_expenses = rent_expense + food_expense + transport_expns + other_expense
remaining_balance = monthly_income - total_expenses
savings_rate = (remaining_balance / monthly_income)

# Display the results
print("=" * 40)
print("MONTHLY BUDGET REPORT")
print("=" * 40)
print(f"Income : ${monthly_income:.2f}")
print("-" * 40)
print("Expenses")
print(f"  Rent: ${rent_expense:.2f}")
print(f"  Food: ${food_expense:.2f}")
print(f"  Transportation: ${transport_expns:.2f}")
print(f"  Other: ${other_expense:.2f}")
print("-" * 40)
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
print(f"Savings Rate: {savings_rate:.2%}")
print("=" * 40)

# Problem 2 - Grade Statistics Calculator
print("\n" + "=" * 40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)

#TODO: Your Code Here
student_amt = int(input("Enter the number of students in the class: "))
grades = []
sum = 0.0
MAXSUM = 0
for i in range(student_amt):
    grade = float(input(f"  Enter grade {i + 1}: "))
    grades.append(grade)
    sum += grade
    MAXSUM += 100

average = sum / student_amt
points_needed_for_90 = (0.9 * MAXSUM) - sum

#Print the results
print("=" * 40)
print("Statistics:")
print(sum, "/", MAXSUM)
print(f"Class Average: {average:.2f}")
print(f"Overall Percentage: {average:.2f}%")
if points_needed_for_90 > 0:
    print(f"Points needed for class to reach 90% overall: {points_needed_for_90:.2f}")
else:
    print("Class has already reached 90% overall.")
print("=" * 40)

# Problem 3 - Time Zone Converter
print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)

# TODO: Your Code Here
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

print("+" + "-" * 38 + "+")
print ("| {:^36} |".format("Current Times"))
print("+" + "-" * 38 + "+")
print ("| {:<10} | {:>10} | {:>10} |".format("Time Zone", "Time", "12-Hour"))
print("| {:-<10} | {:->10} | {:->10} |".format("EST", (str((hour) % 24) + ":" + str(minute)), f"{(hour % 12) if (hour % 12) != 0 else 12}:{minute:02d} {'AM' if hour < 12 else 'PM'}"))
print("| {:-<10} | {:->10} | {:->10} |".format("CST", (str((hour - 1) % 24) + ":" + str(minute)), f"{((hour - 1) % 12) if ((hour - 1) % 12) != 0 else 12}:{minute:02d} {'AM' if (hour - 1) < 12 else 'PM'}"))
print("| {:-<10} | {:->10} | {:->10} |".format("MST", (str((hour - 2) % 24) + ":" + str(minute)), f"{((hour - 2) % 12) if ((hour - 2) % 12) != 0 else 12}:{minute:02d} {'AM' if (hour - 2) < 12 else 'PM'}"))
print("| {:-<10} | {:->10} | {:->10} |".format("PST", (str((hour - 3) % 24) + ":" + str(minute)), f"{((hour - 3) % 12) if ((hour - 3) % 12) != 0 else 12}:{minute:02d} {'AM' if (hour - 3) < 12 else 'PM'}"))
print("+" + "-" * 38 + "+")

# Problem 4 - Recipe Scaler
print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)

og_servings = int(input("Enter the original number of servings: "))
desired_servings = int(input("Enter the desired number of servings: "))
scaling_factor = desired_servings / og_servings

print("Enter 5 ingredients and their quantities:")

ingredients = []
units = []
for i in range(5):
    ingredient = input(f"  Ingredient {i + 1} name: ")
    unit = input(f"  Ingredient {i + 1} unit (e.g., cups, tsp): ")
    quantity = float(input(f"  Ingredient {i + 1} quantity: "))
    scaled_quantity = quantity * scaling_factor
    ingredients.append((ingredient, scaled_quantity))
    units.append(unit)
    print()
print("=" * 40)
print(f"Scaled Recipe for {desired_servings} servings:")
print("=" * 40)
print(f"Scaling Factor: {scaling_factor:.2f}")
print("-" * 40)
print(f"Original recipe {og_servings}:" | f"Scaled recipe {desired_servings}:")
for i in range(5):
    print(f"{ingredients[i][1] / scaling_factor:.2f} {units[i]} {ingredients[i][0]} | {ingredients[i][1]:.2f} {units[i]} {ingredients[i][0]}")
print("=" * 40)