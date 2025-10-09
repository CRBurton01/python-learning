"""
Problem 1: String Processing
Complete each task below.
"""

print("Problem 1: String Processing")

# Given information (DO NOT MODIFY):
full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

# Task 1.1 (3 points): Extract and print the first name only
split_name = full_name.split()
firstname = split_name[0]
print(firstname)
# Task 1.2 (3 points): Extract and print the last name only
lastname = split_name[-1]
print(lastname)
# Task 1.3 (3 points): Create and print initials (J.M.S.)
initials = firstname[0] + "." + split_name[1][0] + "." + lastname[0] + "."
print(initials)
# Task 1.4 (3 points): Check if the email contains "university" (case-insensitive)
contains_university = "university" in email.lower()
print(contains_university)
# Task 1.5 (3 points): Replace all dashes in phone with spaces and print
formatted_phone = phone.replace("-", " ")
print(formatted_phone)
print()

"""
Problem 2: Restaurant Rating Calculator
Calculate based on percentage rating.
"""
print("Problem 2: Restaurant Rating Calculator")

# Task 2.1 (3 points): Get these ratings
atmosphere = 4.5
food = 3.4
service = 2.5
cleanness = 3.0

# Task 2.2 (4 points): Calculate weighted average
# Weights: atmosphere=10%, food=45%, service=20%, cleanness=25%
# Store result in variable 'average'
average = (atmosphere * 0.10) + (food * 0.45) + (service * 0.20) + (cleanness * 0.25)
# Task 2.3 (8 points): Determine restaurant rating
# Use these ranges:
# *****: 4.0 and above
# ****: 3.0-4.0
# ***: 2.0-3.0
# **: 1.0-2.0
# *: below 1.0
# Print both the average and star rating
print(f"Restaurant rating is {average}")
if average >= 4.0:
    print("5 Stars! - *****")
elif average >= 3.0:
    print("4 Stars! - ****")
elif average >= 2.0:
    print("3 Stars - ***")
elif average >= 1.0:
    print("2 Stars - **")
else:
    print("1 Star - *")
print()

"""
Problem 3: Movie Review Number Management
Manage a list of movie review numbers.
"""
print("Problem 3: Movie Review Number Management")

# Task 3.1 (2 points): Create a list with these movie review numbers
numbers = [3, 5, 4, 3, 2, 1, 3]
# Task 3.2 (3 points): Add a new review number of 4 to the end
numbers.append(4)
print(numbers)
# Task 3.3 (3 points): The third review number (4) was entered wrong.
# Change it to 3
numbers[2] = 3
print(numbers)
# Task 3.4 (3 points): Remove the review number 1 from the list
numbers.remove(1)
print(numbers)
# Task 3.5 (3 points): Insert a review number of 3 at position 2
numbers.insert(1, 3)
print(numbers)
# Task 3.6 (3 points): Create and print a sublist of the first 3 numbers
sublist = numbers[0:3]
print(sublist)
# Task 3.7 (3 points): Print:
# - How many movie review numbers
# - The first review number
# - The last review number
print(f"There are {len(numbers)} movie reviews.")
print(f"The first review number is {numbers[0]}.")
print(f"The last review number is {numbers[-1]}.")
print()

"""
Problem 4: Shopping Cart System
Build a basic shopping cart with price checking.
"""
print("Problem 4: Shopping Cart System")

# Initial setup (DO NOT MODIFY):
items = ["bread", "milk", "eggs", "cheese", "apples"]
prices = [2.50, 3.99, 2.99, 5.49, 4.99] # Matching prices for each item
cart = []
cart_total = 0.0

# Task 4.1 (4 points): Add "milk" to cart
# Check if "milk" is in items, find its index, and add to cart
# Also add its price to cart_total
if "milk" in items:
    index = items.index("milk")
    cart.append("milk")
    cart_total += prices[index]
    print(f"Added milk to cart. Current total: ${cart_total:.2f}")
else:
    print("Item 'milk' not found in inventory. Cannot add to cart.")
# Task 4.2 (4 points): Add "eggs" to cart
# Same process as above
if "eggs" in items:
    index = items.index("eggs")
    cart.append("eggs")
    cart_total += prices[index]
    print(f"Added eggs to cart. Current total: ${cart_total:.2f}")
else:
    print("Item 'eggs' not found in inventory. Cannot add to cart.")
# Task 4.3 (4 points): Try to add "cookies" to cart
# Check if it exists first, print appropriate message
if "cookies" in items:
    index = items.index("cookies")
    cart.append("cookies")
    cart_total += prices[index]
    print(f"Added cookies to cart. Current total: ${cart_total:.2f}")
else:
    print("Item 'cookies' not found in inventory. Cannot add to cart.")
# Task 4.4 (4 points): Apply discount
# If cart_total > 6.00, apply 10% discount
# Print the original total and discounted total
if cart_total > 6.00:
    discounted_total = cart_total * 0.90
    print(f"Original total: ${cart_total:.2f}")
    print(f"Discounted total (10% off): ${discounted_total:.2f}")
    cart_total = discounted_total
else:
    print(f"Total (no discount applied): ${cart_total:.2f}")
print()
# Task 4.5 (4 points): Final report
# Print:
# - Items in cart
# - Number of items
# - Final total (with discount if applicable)
print("Final Shopping Cart Report:")
print(f"Items in cart: {cart}")
print(f"Number of items: {len(cart)}")
print(f"Final total: ${cart_total:.2f}")