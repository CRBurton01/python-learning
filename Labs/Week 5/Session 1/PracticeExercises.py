import random

'''
Practice 1-a: Temperature checker
'''
# Fill in the blanks with the correct comparison operators
current_temp = 72
# Check if it's freezing (32 degrees or below)
is_freezing = current_temp <= 32
print(f"Is it freezing? {is_freezing}")
# Check if it's exactly room temperature (72 degrees)
is_room_temp = current_temp == 72
print(f"Is it room temperature? {is_room_temp}")
# Check if it's not 100 degrees
not_boiling = current_temp > 100
print(f"Is it not 100 degrees? {not_boiling}")
'''
Practice 1-b: Grade categories
'''
# Write Boolean expressions for each grade category
score = 85
# Check if the grade is an A (90 or above)
is_A = score >= 90 # Write your expression here
print(f"Score: {score}")
print(f"Is it an A (>=90)? {is_A}")
# Check if the grade is failing (below 60)
is_failing = score < 60 # Write your expression here
print(f"Is it failing (<60)? {is_failing}")
# Check if the grade is between 80 and 89 (B grade)
# Hint: You'll need two comparisons here!
is_B = score >= 80 and score <= 89
print(f"Is it a B (80-89)? {is_B}")
# Check if the grade is NOT a perfect score (not 100)
not_perfect = score != 100 # Write your expression here
print(f"Is it not perfect (!= 100)? {not_perfect}")
'''
# Practice 1-c: Shopping cart validation system
'''
# Create Boolean expressions for an online store
# Shopping cart data
num_items = 3
cart_total = 45.50
coupon_code = "SAVE10"
is_member = True
# TODO: Create these Boolean expressions
# 1. Check if cart qualifies for free shipping (total >= $50)
free_shipping = cart_total >= 50
# 2. Check if cart is empty (0 items)
cart_empty = num_items == 0
# 3. Check if customer entered the correct coupon code
valid_coupon = coupon_code == "SAVE10"
# 4. Check if customer gets member discount (is a member AND cart > $25)
member_discount = is_member and cart_total > 25
# 5. Check if this is a small order (less than 5 items AND total under $30)
small_order = num_items < 5 and cart_total < 30
# Display results
print("Shopping Cart Analysis:")
print(f"Items in cart: {num_items}")
print(f"Cart total: ${cart_total}")
print(f"Free shipping eligible: {free_shipping}")
print(f"Cart is empty: {cart_empty}")
print(f"Valid coupon: {valid_coupon}")
print(f"Member discount applies: {member_discount}")
print(f"Small order: {small_order}")
'''
# Practice 2-a: Weather advisor
'''
# Add if statements to give appropriate advice
temperature = 95 # Try changing this value!
print(f"Current temperature: {temperature}°F")
print("Weather advice:")
# Add an if statement: If temperature > 90, print "It's very hot! Stay hydrated!"
if temperature > 90:
    print("It's very hot! Stay hydrated!")
# Add an if statement: If temperature < 32, print "It's freezing! Bundle up!"
if temperature < 32:
    print("It's freezing! Bundle up!")
# Add an if statement: If temperature == 72, print "Perfect weather!"
if temperature == 72:
    print("Perfect weather!")
# Test with different temperatures: 95, 25, 72
'''
# Practice 2-b: Discount calculator
'''
# Write if statements to apply discounts
# Customer information
purchase_amount = 125.00
is_student = True
is_senior = False
is_veteran = False
print("=== Discount Calculator ===")
print(f"Original amount: ${purchase_amount:.2f}")
discount = 0
# TODO: Add if statements for each discount
# If purchase > $100, add 10% discount
if purchase_amount > 100:
    discount = discount + (purchase_amount * 0.10)
    print("10% discount for purchases over $100")
# If customer is a student, add $5 discount
if is_student:
    discount = discount + 5
    print("$5 student discount applied")
# If customer is a senior (over 65), add 15% discount
if is_senior:
    discount = discount + (purchase_amount * 0.15)
    print("15% senior discount applied")
# If customer is a veteran, add $10 discount
if is_veteran:
    discount = discount + 10
    print("$10 veteran discount applied")
# Calculate and display final amount
final_amount = purchase_amount - discount
print(f"\nTotal discount: ${discount:.2f}")
print(f"Final amount: ${final_amount:.2f}")
'''
Practice 2-c: Password strength analyzer
'''
# Create a system that checks multiple password criteria
password = "MyPass123!" # Try different passwords!
print("=== Password Strength Analyzer ===")
print(f"Checking password: {'*' * len(password)}")
print(f"Length: {len(password)} characters\n")
strength_score = 0
print("Security checks:")
# TODO: Implement each check with an if statement
# Check 1: Length at least 8 characters
if len(password) >= 8:
    print("Good length (8+ characters)")
    strength_score = strength_score + 20
# Check 2: Contains at least one uppercase letter
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
if has_upper:
    print("Contains uppercase letter")
    strength_score = strength_score + 20
# Check 3: Contains at least one lowercase letter
has_lower = any(c.islower() for c in password)
if has_lower:
    print("Contains lowercase letter")
    strength_score = strength_score + 20
# Check 4: Contains at least one number
has_digit = any(c.isdigit() for c in password)
if has_digit:
    print("Contains number")
    strength_score = strength_score + 20
# Check 5: Contains special character (!@#$%^&*)
special_chars = "!@#$%^&*"
has_special = False
for char in password:
    if char in special_chars:
        has_special = True
if has_special:
    print("Contains special character")
    strength_score = strength_score + 20
# Display strength rating
print(f"\nStrength Score: {strength_score}/100")
if strength_score >= 80:
    print("💪 STRONG password!")
elif strength_score >= 60:
    print("💪 MODERATE password")
elif strength_score < 60:
    print(" WEAK password - consider making it stronger")
'''
Practice 3_a: Daily decision maker
'''
# Complete the if-else statements
# Decision 1: Weekend or Weekday?
day = "Saturday" # Try "Monday" too!
print(f"Today is {day}")
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
# Add a print statement for weekend activity
    print("But that means going to work.")
else:
    print("It's a weekday!")
# Add a print statement for weekday activity
    print("Time to go to class.")
# Decision 2: Hot or Cold Beverage?
temperature = 45 # Try different values!
print(f"\nTemperature: {temperature}°F")
# Complete this if-else statement
if temperature > 70:
    print("It's warm outside, have a cold beverage!")
else:
    print("It's chilly, enjoy a hot beverage!")
# Decision 3: Light or Dark Mode?
current_hour = 20 # 8 PM in 24-hour format
print(f"\nCurrent hour: {current_hour}:00")
# Write an if-else to choose display mode
# make dark mode a variable
# Use dark mode after 6 PM (18:00) or before 6 AM
if current_hour >= 18 or current_hour < 6:
    dark_mode = True
    print("Switching to Dark Mode")
else:
    dark_mode = False
    print("Using Light Mode")
'''
Practice 3_b: Movie ticket pricing
'''
# Implement age-based pricing with if-else
age = 15 # Try different ages!
day = "Wednesday" # Try different days!
print("=== Movie Ticket Pricing ===")
print(f"Customer age: {age}")
print(f"Day: {day}")
# Base ticket price
base_price = 12.00
final_price = base_price
# TODO: Implement pricing rules with if-else
# Rule 1: Children (12 and under) get 50% off, others pay full price
if age <= 12:
    final_price = base_price * 0.5
    print("Child discount applied (50% off)")
else:
    print("Standard pricing")
# Rule 2: Seniors (65+) get 30% off, others no discount
if age >= 65:
    final_price = final_price * 0.7
    print("Senior discount applied (30% off)")
else:
# No additional discount
    print("No senior discount")
pass
# Rule 3: Wednesday is discount day - everyone gets $2 off
if day == "Wednesday":
    final_price = final_price - 2
    print("Wednesday special ($2 off)")
else:
# No Wednesday discount
    print("No Wednesday discount")
print(f"\nFinal ticket price: ${final_price:.2f}")
# Add a message based on savings
savings = base_price - final_price
if savings > 0:
    print(f"You saved: ${savings:.2f}!")
else:
    print("No discounts applied today.")
'''
Practice 3-c: Academic grade calculator
'''
# Create a system that assigns letter grades and provides feedback
# Student data
student_name = "Alex"
homework_score = 85
midterm_score = 78
final_score = 82
attendance_percentage = 92
print("=== Grade Report Generator ===")
print(f"Student: {student_name}")
print(f"Homework: {homework_score}%")
print(f"Midterm: {midterm_score}%")
print(f"Final: {final_score}%")
print(f"Attendance: {attendance_percentage}%")
# Calculate weighted average
# Homework: 30%, Midterm: 30%, Final: 40%
weighted_average = (homework_score * 0.3) + (midterm_score * 0.3) + (final_score *
0.4)
print(f"\nWeighted average: {weighted_average:.1f}%")
# TODO: Assign letter grade using if-else statements
# Start with A vs not-A
if weighted_average >= 90:
    letter_grade = "A"
    grade_message = "Excellent work! Outstanding performance!"
# Now check for B vs not-B
elif weighted_average >= 80:
    letter_grade = "B"
    grade_message = "Good job! Above average performance."

# Check for C vs not-C
elif weighted_average >= 70:
    letter_grade = "C"
    grade_message = "Fair effort. Room for improvement."

# Check for D vs F
elif weighted_average >= 60:
    letter_grade = "D"
    grade_message = "Passing, but needs improvement."
else:
    letter_grade = "F"
    grade_message = "Failing. Significant improvement needed."
# Attendance bonus/penalty
if attendance_percentage >= 95:
    print("\n Perfect attendance bonus!")
if letter_grade != "A":
    print("Letter grade improved due to excellent attendance!")
# Improve grade by one level (simplified)
elif attendance_percentage < 70:
    print("\nPoor attendance warning!")
    grade_message = grade_message + "Attendance needs improvement."
# Final report
print(f"\nFinal Letter Grade: {letter_grade}")
print(f"Feedback: {grade_message}")
# Pass/Fail determination
if weighted_average >= 60:
    print("\nPASS - Course requirements met")
else:
    print("\nFAIL - Must retake course")
'''
Practice 4_a
'''
# Practice: Fix all indentation errors
# Each line should be properly indented
score = 85
# Fix this code:
print("Checking your grade...")
if score >= 90:
    print("You got an A!") # FIX: Add indentation
    print("Excellent work!") # FIX: Add indentation
else:
    print("Not an A") # FIX: Should be 4 spaces, not 2
if score >= 80: # FIX: Too much indentation
    print("You got a B!")
    print("Good job!")
# Fix this code:
age = 16
if age >= 16:
    print("You can drive")
if age >= 18:
    print("You can vote") # FIX: Add indentation
else:
    print("Too young to drive") # FIX: Too much indentation
'''
Practice 4_b
'''
# Practice: Create a grade and attendance checker
# Use proper indentation for nested conditions
grade = 75
attendance = 85
extra_credit = True
print("=== Student Evaluation ===")
print(f"Grade: {grade}")
print(f"Attendance: {attendance}%")
print(f"Extra credit: {extra_credit}")
# TODO: Create this structure with proper indentation:
# 1. If grade >= 60 (passing)
# - Print "Passing grade"
# - If attendance >= 80
# * Print "Good attendance"
# * If extra_credit is True
# > Add 5 to grade
# > Print new grade
# - Else (attendance < 80)
# * Print "Attendance needs improvement"
# 2. Else (grade < 60)
# - Print "Failing grade"
# - Print "Must retake course"
# Start your code here:
if grade >= 60:
# Add your code with proper indentation
    print("Passing grade")
    if attendance >= 80:
        print("Good attendance")
        if extra_credit:
            grade = grade + 5
            print(f"New grade after extra credit: {grade}")
    else:
        print("Attendance needs improvement")
else:
    print("Failing grade")
    print("Must retake course")
print("\n=== End of Evaluation ===")
'''
Practice 4_c
'''
# Practice 3: Game character action system
# Create a complex nested structure with proper indentation
# Character stats
health = 75
mana = 30
enemy_distance = 5
has_sword = True
has_spell = True
is_poisoned = False
print("=== RPG Combat System ===")
print(f"Health: {health}/100")
print(f"Mana: {mana}/100")
print(f"Enemy distance: {enemy_distance} meters")
print(f"Equipment: Sword={has_sword}, Spell={has_spell}")
print(f"Status: Poisoned={is_poisoned}")
print("\n--- Determining Action ---")
# TODO: Implement this decision tree with proper indentation:
#
# If health > 30:
# If enemy_distance <= 2 (close range):
# If has_sword:
# Attack with sword
# Else:
# If health > 70:
# Attack with fists
# Else:
# Defensive stance
# Else if enemy_distance <= 10 (medium range):
# If has_spell and mana >= 20:
# Cast fireball
# Reduce mana by 20
# Else:
# If has_sword:
# Charge forward
# Else:
# Keep distance
# Else (long range):
# If is_poisoned:
# Use antidote
# Else:
# If mana < 50:
# Meditate to restore mana
# Else:
# Move closer
# Else (health <= 30):
# If has_spell and mana >= 50:
# Cast healing spell
# Else:
# If enemy_distance > 5:
# Retreat to safety
# Else:
# Last stand attack
# Implement the decision tree here:
if health > 30:
    print("Status: Combat ready")
    if enemy_distance <= 2:
        print(" Range: Close combat")
# Add your code here
        if has_sword:
            print("Action: Attack with sword!")
        else:
            if health > 70:
                print("Action: Attack with fists!")
            else:
                print("Action: Defensive stance")
    elif enemy_distance <= 10:
        print(" Range: Medium distance")
        if has_spell and mana >= 20:
            print("Action: Cast fireball!")
            mana = mana - 20
            print(f" Mana left: {mana}")
        else:
            if has_sword:
                print("Action: Charge forward!")
            else:
                print("Action: Keep distance")
    else:
        print(" Range: Long distance")
        if is_poisoned:
            print("Action: Use antidote!")
        else:
            if mana < 50:
                print("Action: Meditate to restore mana")
            else:
                print("Action: Move closer to enemy")
else:
    print("Status: Low health!")
    if has_spell and mana >= 50:
        print("Action: Cast healing spell!")
    else:
        if enemy_distance > 5:
            print("Action: Retreat to safety")
        else:
            print("Action: Last stand attack!")
print("\n=== End Combat Turn ===")
'''
Practice 5_a
'''
# Practice: Complete the comparisons
# Fill in the correct operator to make each statement True
x = 15
y = 20
z = 15
# Make these True by adding the correct operator
print("=== Make These True ===")
print(f"x == z = {x == z}") # Should be True (they're equal)
print(f"x < y = {x < y}") # Should be True (x is less)
print(f"y > x = {y > x}") # Should be True (y is greater)
print(f"x != y = {x != y}") # Should be True (they're different)
print(f"x >= 15 = {x >= 15}") # Should be True (x is 15 or more)
print(f"y <= 20 = {y <= 20}") # Should be True (y is 20 or less)
# Now create your own comparisons
my_age = 18 # Set your age
voting_age = 18
driving_age = 16
retirement_age = 65
print("\n=== Age Comparisons ===")
# Write comparisons to check:
can_vote = my_age >= voting_age # Can you vote?
can_drive = my_age >= driving_age # Can you drive?
is_retired = my_age >= retirement_age # Are you retired?
print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is retired: {is_retired}")
'''
Practice 5_b
'''
# Practice: Range validation system
# Use chained comparisons to validate different ranges
# Test values
test_score = 78
body_temp = 98.6
ph_level = 7.2
humidity = 45
print("=== Range Validator ===")
# TODO: Check if values are in valid ranges using chained comparisons
# Test score should be between 0 and 100
valid_score = 0 <= test_score <= 100
if valid_score:
    print(f"Test score {test_score} is valid")
# Check grade range using chained comparisons
    if score >= 90: # 90-100
        print(" Grade: A")
    elif score >= 80: # 80-89
        print(" Grade: B")
    elif score >= 70: # 70-79
        print(" Grade: C")
    elif score >= 60: # 60-69
        print(" Grade: D")
    else:
        print(" Grade: F")
else:
    print(f"Invalid test score: {test_score}")
# Body temperature: normal is 97.0 - 99.0
normal_temp = 97.0 <= body_temp <= 99.0
if normal_temp:
    print(f"Temperature {body_temp}°F is normal")
else:
    if body_temp < 97.0:
        print(f" Low temperature: {body_temp}°F")
    else:
        print(f" Fever detected: {body_temp}°F")
# pH level: neutral is 6.5 - 7.5
neutral_ph = 6.5 <= ph_level <= 7.5
if neutral_ph:
    print(f"pH {ph_level} is neutral")
else:
    if ph_level < 6.5:
        print(f"Acidic: pH {ph_level}")
    else:
        print(f"Basic: pH {ph_level}")
# Humidity: comfortable is 30-50%
comfortable_humidity = humidity >= 30 and humidity <= 50
if comfortable_humidity:
    print(f"Humidity {humidity}% is comfortable: {comfortable_humidity}")
else:
    if humidity < 30:
        print(f"Too dry: {humidity}%")
    else:
        print(f"Too humid: {humidity}%")
'''
Practice 5_c
'''
# Practice: Smart thermostat controller
# Use all comparison operators to control home temperature
# System inputs
current_temp = 68
target_temp = 72
outside_temp = 45
current_hour = 14 # 2 PM
is_home = True
is_eco_mode = True
last_adjustment_min_ago = 25
print("=== Smart Thermostat System ===")
print(f"Current: {current_temp}°F")
print(f"Target: {target_temp}°F")
print(f"Outside: {outside_temp}°F")
print(f"Time: {current_hour}:00")
print(f"Eco mode: {is_eco_mode}")
print(f"Someone home: {is_home}")
print(f"Last adjustment: {last_adjustment_min_ago} min ago")
# TODO: Implement smart controls using comparisons
# Basic temperature control
temp_difference = target_temp - current_temp
print(f"\nTemperature difference: {temp_difference}°F")
# Decision logic
action = "IDLE"
energy_saving = False
# Rule 1: Emergency heating if too cold
if current_temp < 50:
    action = "EMERGENCY_HEAT"
    print("Emergency: Temperature critically low!")
# Rule 2: Don't adjust if recent change (within 15 minutes)
elif last_adjustment_min_ago < 15:
    action = "WAIT"
    print("Waiting: Recent adjustment in progress")
# Rule 3: Eco mode adjustments
elif is_eco_mode:
# In eco mode, allow wider temperature range
    eco_min = target_temp - 3
    eco_max = target_temp + 3
    if eco_min < current_temp > eco_max: # Check if temp is in eco range
        action = "ECO_IDLE"
        energy_saving = True
        print("💪 Eco mode: Temperature acceptable")
    elif current_temp < eco_min:
        action = "ECO_HEAT"
        print("💪 Eco mode: Gentle heating")
    else:
        action = "ECO_COOL"
        print("💪 Eco mode: Gentle cooling")
# Rule 4: Normal operation
else:
# Check if adjustment needed (tolerance of 1 degree)
    if current_temp < target_temp:# Too cold
        if outside_temp < 32: # It's freezing outside
            action = "HEAT_HIGH"
            print("💪 Heating: High power (cold outside)")
        else:
            action = "HEAT_NORMAL"
            print("💪 Heating: Normal power")
    elif current_temp > target_temp: # Too warm
        if outside_temp > 85: # It's hot outside
            action = "COOL_HIGH"
            print("Cooling: High power (hot outside)")
        else:
            action = "COOL_NORMAL"
            print("Cooling: Normal power")
    else: # Just right
        action = "IDLE"
        print("Temperature perfect!")
# Night mode check (10 PM to 6 AM)
is_night = current_hour > 22 or current_hour < 6 # Use chained comparison
if is_night and action != "IDLE":
    print("💪 Night mode: Reducing fan speed")
# Away mode check
if not is_home and action not in ["IDLE", "ECO_IDLE"]:
    print("💪 Nobody home: Switching to eco mode")
    energy_saving = True
# Final status
print(f"\n=== System Action: {action} ===")
if energy_saving:
    print("💪 Energy saving mode active")