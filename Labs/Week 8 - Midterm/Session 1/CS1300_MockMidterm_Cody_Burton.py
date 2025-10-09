'''
Problem 1: Student ID Processing
Complete each task below.
'''

print()
print("Problem 1: Student ID Processing")
# Given information (DO NOT MODIFY)
student_id = "2025-CS-0342"
student_email = "SMITH.JANE@SCHOOL.EDU"
course_code = "CS1300-001"

#Task 1.1 (3 points): Extract and print the year from the student_id variable (2025)
student_id_parts = student_id.split('-')
year = student_id_parts[0]
print("Year:", year)

#Task 1.2 (3 points): Extract and print the student number only (0342)
student_number = student_id_parts[2]
print("Student Number:", student_number)

#Task 1.3 (3 points): Convert the student_email to lowercase and extract username before @
student_email_lower = student_email.lower()
username = student_email_lower.split('@')[0]
print("Username:", username)

#Task 1.4 (3 points): Check if course code starts with "CS"
is_cs_course = course_code.startswith("CS")
print("Is CS Course:", is_cs_course)

#Task 1.5 (3 points): Create new ID format: "year_number" (like "2025_0342")
new_id_format = f"{year}_{student_number}"
print("New ID Format:", new_id_format)

'''
Problem 2: Restaurant Bill Calculator
Calculate total bill including tax and tip.
'''

print()
print("Problem 2: Restaurant Bill Calculator")
# Task 2.1 (3 points): Set these amounts
food_total = 45.50
drinks_total = 18.75
dessert_total = 12.25

# Task 2.2 (4 points): Calculate subtotal and add tax (8%)
subtotal = food_total + drinks_total + dessert_total
tax = subtotal * 0.08
total_with_tax = subtotal + tax

# Task 2.3 (8 points): Calculate total with tip
# If service is excellent (total >= 50), tip is 20%
# If service is good (total >= 30), tip is 18%
# If service is okay (total >= 15), tip is 15%
# Otherwise, tip is 10%
if total_with_tax >= 50:
    tip_percentage = 0.20
elif total_with_tax >= 30:
    tip_percentage = 0.18
elif total_with_tax >= 15:
    tip_percentage = 0.15
else:
    tip_percentage = 0.10

#Calculate and print:
# - Subtotal
# - Tax amount
# - Tip amount
# - Final total

tip_amount = total_with_tax * tip_percentage
final_total = total_with_tax + tip_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Tip: ${tip_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")

'''
Problem 3: Product Inventory
Manage a list of products in stock.
'''

print()
print("Problem 3: Product Inventory")
# Task 3.1 (2 points): Create initial inventory
products = ["laptop", "mouse", "keyboard", "monitor", "cable"]

# Task 3.2 (3 points): Add "headphones" to the inventory
products.append("headphones")
print("Inventory after adding headphones:", products)

# Task 3.3 (3 points): A customer returned a "webcam"
# Insert it at position 3
products.insert(3, "webcam")
print("Inventory after adding webcam:", products)

# Task 3.4 (4 points): "cable" is out of stock, remove it
products.remove("cable")
print("Inventory after removing cable:", products)

# Task 3.5 (3 points): Replace "mouse" with "wireless mouse"
# Find its index first, then update
mouse_index = products.index("mouse")
products[mouse_index] = "wireless mouse"
print("Inventory after replacing mouse with wireless mouse:", products)

# Task 3.6 (5 points): Get and print the last 3 items in the inventory
last_three_items = products[-3:]
print("Last three items in inventory:", last_three_items)

# Task 3.7 (5 points): Create a display showing:
# - Total products in stock
# - First product alphabetically
# - Products at even indices (0, 2, 4...)
total_products = len(products)
first_product = sorted(products)[0]
even_indexed_products = products[0::2]

print(f"Total products in stock: {total_products}")
print(f"First product alphabetically: {first_product}")
print(f"Products at even indices: {even_indexed_products}")

'''
Problem 4: Gym Membership Calculator
Calculate membership fees with discounts.
'''

print()
print("Problem 4: Gym Membership Calculator")
# Initial setup (DO NOT MODIFY):
membership_types = ["basic", "standard", "premium", "vip"]
monthly_prices = [29.99, 49.99, 79.99, 99.99]
selected_plan = []
total_cost = 0

# Task 4.1 (4 points): Customer selects "standard" plan
# Check if it exists, add to selected_plan, and update total_cost
if "standard" in membership_types:
    selected_plan.append("standard")
    plan_index = membership_types.index("standard")
    total_cost += monthly_prices[plan_index]
print("Selected Plan:", selected_plan)
print(f"Total Cost after selecting standard plan: ${total_cost:.2f}")
print()
# Task 4.2 (4 points): Customer adds "yoga" class
# Check if "yoga" is in membership_types (it's not)
# Print appropriate message
if "yoga" in membership_types:
    selected_plan.append("yoga")
else:
    print("Plan 'yoga' does not exist. Cannot add to selected plan.")
print()
# Task 4.3 (4 points): Customer upgrades to "premium"
# Clear selected_plan, add "premium"
# Calculate new cost for 3 months
months = 3
selected_plan.clear()
if "premium" in membership_types:
    selected_plan.append("premium")
    plan_index = membership_types.index("premium")
    total_cost = monthly_prices[plan_index] * 3
print("Selected Plan after upgrade:", selected_plan)
print(f"Total Cost for 3 months of premium: ${total_cost:.2f}")
print()
# Task 4.4 (4 points): Apply discounts
# If total_cost > 200, apply 15% discount
# If total_cost > 150, apply 10% discount
# Otherwise, no discount
# Print original and discounted amount

print("Original Total Cost before discount: ${:.2f}".format(total_cost))

if total_cost > 200:
    discount = total_cost * 0.15
    total_cost -= discount
    print(f"Applied 15% discount of ${discount:.2f}")
elif total_cost > 150:
    discount = total_cost * 0.10
    total_cost -= discount
    print(f"Applied 10% discount of ${discount:.2f}")
else:
    print("No discount applied.")

print(f"Final Total Cost after discount: ${total_cost:.2f}")
print()
# Task 4.5 (4 points): Final summary
# Print:
# - Selected plan
# - Duration in months
# - Final total cost after discounts
print("Final Summary:")
print(f"Selected Plan: {selected_plan}")
print(f"Duration: {months} months")
print(f"Final Total Cost after discounts: ${total_cost:.2f}")

