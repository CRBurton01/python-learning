# PROBLEM 1 - Temperature Converter & Weather Advisor
print("=== Temperature Converter & Weather Advisor ===")
advice = ""
# Get temperature from user
temp = float(input("Enter temperature: "))
# Get the scale (C or F)
scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()
# YOUR CODE HERE
# 1. Check which scale was entered
# 2. Convert to the other scale
# 3. Display both temperatures
# 4. Give weather advice based on Fahrenheit
if scale == 'C':
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C is {fahrenheit:.2f}°F")
    if fahrenheit < 32:
        advice = "Freezing! Bundle up warmly!"
    elif 32 <= fahrenheit < 50:
        advice = "Cold - wear a warm jacket."
    elif 50 <= fahrenheit < 70:
        advice = "Cool - A light jacket should be fine."
    elif 70 <= fahrenheit < 85:
        advice = "Pleasant - enjoy the weather!"
    else:
        advice = "Hot - Stay hydrated!"
elif scale == 'F':
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F is {celsius:.2f}°C")
    if temp < 32:
        advice = "Freezing! Bundle up warmly!"
    elif 32 <= temp < 50:
        advice = "Cold - wear a warm jacket."
    elif 50 <= temp < 70:
        advice = "Cool - A light jacket should be fine."
    elif 70 <= temp < 85:
        advice = "Pleasant - enjoy the weather!"
    else:
        advice = "Hot - Stay hydrated!"
print(advice)

# PROBLEM 2 - Movie Theater Ticket System
print("=== Movie Theater Ticket System ===")
# Get customer information
age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()

# YOUR CODE HERE
# Remember:
# - Check for Tuesday special first
# - If not Tuesday, ask for show time
# - Apply age-based pricing
# - Apply matinee discount if applicable
if day == "tuesday":
    price = 7.00
else:
    time = int(input("Enter show time (24-hour format): "))
    if age <= 12:
        price = 8.00
    elif 13 <= age <= 64:
        price = 15.00
        if time < 16:
            price -= 3.00
    else:  # age >= 65
        price = 10.00
        if time < 16:
            price -= 3.00
print(f"Ticket price: ${price:.2f}")

# PROBLEM 3 - Grade Calculator
print("=== Grade Calculator ===")
# Get three test scores
test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))
# YOUR CODE HERE
# 1. Validate all scores are between 0 and 100
# 2. If invalid, print error and stop
# 3. Calculate average
# 4. Determine letter grade using elif
# 5. Check passing criteria (D or better AND at least one test >= 60)
# 6. Display results
if not (0 <= test1 <= 100) or not (0 <= test2 <= 100) or not (0 <= test3 <= 100):
    print("Error: All test scores must be between 0 and 100.")
else:
    average = (test1 + test2 + test3) / 3
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    passing = (grade != 'F') and (test1 >= 60 or test2 >= 60 or test3 >= 60)
    print(f"Average score: {average:.2f}")
    print(f"Letter grade: {grade}")
    if passing:
        print("Status: Passing")
    else:
        print("Status: Failing")
        
# PROBLEM 4 - Password Strength Checker
print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")
# Initialize criteria counters
criteria_met = 0
feedback = []
# YOUR CODE HERE
# 1. Check each criterion
# 2. For each criterion met, increment criteria_met
# 3. For each criterion not met, add feedback message
# 4. Determine strength level

# Hint for checking digits:
#has_digit = any(char.isdigit() for char in password)
if len(password) >= 8:
    criteria_met += 1
else:
    feedback.append("Password should be at least 8 characters long. ")
if any(char.isupper() for char in password):
    criteria_met += 1
else:
    feedback.append("Password should include at least one uppercase letter. ")
if any(char.islower() for char in password):
    criteria_met += 1
else:
    feedback.append("Password should include at least one lowercase letter. ")
if any(char.isdigit() for char in password):
    criteria_met += 1
else:
    feedback.append("Password should include at least one digit. ")
if password == "password" or password == "12345678" or password == "qwerty":
    feedback.append("Password is too common. ")
else:
    criteria_met += 1
# Determine strength
if criteria_met == 5:
    strength = "Strong"
elif criteria_met == 4:
    strength = "Good"
elif criteria_met == 3:
    strength = "Fair"
else:
    strength = "Weak"
print(f"Password strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for msg in feedback:
        print("-", msg)
else:
    print("Your password meets all the criteria!")
    
# PROBLEM 5 - Restaurant Bill Calculator
print("=== Restaurant Bill Calculator ===")
# Get initial information
surcharge = 0.0
has_senior = "no"
gratuity = 0.0
mem_discount = 0.0
sen_discount = 0.0
food_total = float(input("Enter food total: $"))
is_holiday = input("Is today a holiday? (yes/no): ").lower()
party_size = int(input("How many people in your party? "))
is_member = input("Are you a member? (yes/no): ").lower()
day = input("Enter day of the week: ").lower()
# YOUR CODE HERE
# Follow the requirements and calculation order
# Remember to ask additional questions based on conditions
# Display a detailed breakdown of the bill
if is_holiday == "yes":
    surcharge =+ 0.15 * food_total
if party_size > 6:
    gratuity = 0.18 * food_total
if is_member == "yes":
    mem_discount = 0.10 * food_total
if day == "wednesday":
    has_senior = input("Is anyone in your party a senior citizen? (yes/no): ").lower()
    if has_senior == "yes":
        sen_discount = 0.10 * food_total
print()
print("--- Bill Breakdown ---")
# Calculate totals
print(f"Food Total: ${food_total:.2f}")
if surcharge > 0:
    print(f"Holiday Surcharge (15%): ${surcharge:.2f}")
if party_size > 6:
    print(f"Gratuity (18%): ${gratuity:.2f}")
if is_member == "yes":
    print(f"Member Discount (10%): -${mem_discount:.2f}")
if has_senior == "yes":
    print(f"Senior Discount (10%): -${sen_discount:.2f}")
subtotal = food_total + surcharge + gratuity - mem_discount - sen_discount
print(f"Subtotal: ${subtotal:.2f}")
tax = 0.085 * subtotal
print(f"Tax (8.5%): ${tax:.2f}")
total = subtotal + tax
print(f"Total Bill: ${total:.2f}")
print()
print("Thank you for dining with us!")

# End of Homework 4