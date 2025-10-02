"""
CS1300 - Homework #5: Advanced Control Structures
Name: Cody Burton
Date: October 2, 2025
Description: Advanced conditional logic and validation
"""

# PROGRAM 1: Smart Thermostat System
def Smart_Thermostat():
    print("=== SMART THERMOSTAT SYSTEM ===")
    # Get inputs
    current_temp = float(input("Current temperature (F): "))
    desired_temp = float(input("Desired temperature (F): "))
    hour = int(input("Current hour (0-23): "))
    season = input("Season (summer/winter/spring/fall): ").lower()
    print()
    # YOUR CODE HERE
    # 1. Check if current temp is in comfortable range using chained comparison
    if  68 <= current_temp <= 76:
        print(f"Current temperature is {current_temp}. No adjustments needed.")
    elif current_temp < 68:
        print(f"Current temperature is {current_temp}. Heating cycle starting.")
    elif current_temp > 76:
        print(f"Current temperature is {current_temp}. Cooling cycle starting.")
    # 2. Determine if it's night time (22-6)
    if hour >= 22 or hour <= 6:
        print("It's night time. Adjusting temperature for sleep comfort. (-3F adjustment)")
        if desired_temp < 65:
            desired_temp = 65
        elif desired_temp > 73:
            desired_temp = 73
        print(f"Adjusted desired temperature for night: {desired_temp}F")
    # 3. Apply seasonal restrictions
    if season == "summer":
        print("Summer mode: Minimum desired temperature set to 75F.")
        if desired_temp < 75:
            desired_temp = 75    
    elif season == "winter":
        print("Winter mode: Maximum desired temperature set to 70F.")
        if desired_temp > 70:
            desired_temp = 70    
    elif season in ["spring", "fall"]:
        print("Spring/Fall mode: Min/Max desired temperature set to 68F/74F.")
        if desired_temp < 68:
            desired_temp = 68
        elif desired_temp > 74:
            desired_temp = 74
    # 4. Calculate actual target temperature after adjustments
    print()
    print(f"Final desired temperature: {desired_temp}F")
    # 5. Calculate time to reach target
        # 5 minutes per degree change
    temp_diff = abs(desired_temp - current_temp)
    time_to_reach = temp_diff * 5 
    print(f"Estimated time to reach target temperature: {time_to_reach} minutes")
    # 6. Determine energy efficiency (Excellent/Good/Fair/Poor)
    if temp_diff <= 2:
        efficiency = "Excellent"
    elif 2 < temp_diff <= 5:
        efficiency = "Good"
    elif 5 < temp_diff <= 10:
        efficiency = "Fair"
    else:
        efficiency = "Poor"
    # Hint: Use chained comparisons like: 68 <= current_temp <= 76
    # Hint: Night check needs: hour >= 22 or hour <= 6

    print(f"Energy efficiency rating: {efficiency}")

# PROGRAM 2: Password Security Analyzer
def Password_Security():
    print("=== PASSWORD SECURITY ANALYZER ===")
    password = input("Enter password to analyze: ")
    print()
    # Initialize score
    score = 0
    # YOUR CODE HERE
    # Use conditional expressions for each check
    # Example: length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
    # Check length (use conditional expression)
    length_points = 30 if len(password) >= 16 else 20 if len(password) >= 12 else 10 if len(password) >= 8 else 0
    # Check for uppercase (use conditional expression)
    has_upper = password != password.lower()
    upper_points = 20 if has_upper else 0
    # Check for lowercase
    has_lower = password != password.upper()
    lower_points = 20 if has_lower else 0
    # Check for numbers
    has_digit = any(c.isdigit() for c in password)
    digit_points = 20 if has_digit else 0
    # Check for special characters
    has_special = not password.isalnum()
    special_points = 10 if has_special else 0
    # Check for common patterns
    common_patterns = ["123", "abc", "qwerty", "password", "111"]
    has_pattern = any(pattern in password.lower() for pattern in common_patterns)
    pattern_points = -20 if has_pattern else 0
    # Calculate total score and determine strength level
    score = length_points + upper_points + lower_points + digit_points + special_points + pattern_points
    if score >= 80:
        strength = "Very Strong"
    elif 60 <= score < 80:
        strength = "Strong"
    elif 40 <= score < 60:
        strength = "Moderate"
    elif 20 <= score < 40:
        strength = "Weak"
    else:
        strength = "Very Weak"
    # Display detailed analysis
    print(f"\nPassword Analysis:")
    print(f"Length points: {length_points}")
    print(f"Uppercase points: {upper_points}")
    print(f"Lowercase points: {lower_points}")
    print(f"Digit points: {digit_points}")
    print(f"Special character points: {special_points}")
    print(f"Common pattern penalty: {pattern_points}")
    print()
    print(f"Total Score: {score}")
    print(f"Password Strength: {strength}")

# PROGRAM 3: Student Grade Validator
def Grade_Validator():
    print("=== GRADE VALIDATION SYSTEM ===")
    # Get four test scores
    test1 = float(input("Test 1 score: "))
    test2 = float(input("Test 2 score: "))
    test3 = float(input("Test 3 score: "))
    test4 = float(input("Test 4 score: "))
    # YOUR CODE HERE
    # 1. Validate each score is 0-100 using chained comparisons
    all_valid_range = (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100) and (0 <= test4 <= 100)
    # 2. Check for suspicious patterns
    huge_jump = (abs(test2 - test1) > 30) or (abs(test3 - test2) > 30) or (abs(test4 - test3) > 30)
    all_identical = (test1 == test2 == test3 == test4)
    # 3. Use truth table logic:
    valid_range = all_valid_range
    not_suspicious = not huge_jump
    not_identical = not all_identical
    # 4. If valid, calculate average, highest, lowest, improvement
    if valid_range and not_suspicious and not_identical:
        average = (test1 + test2 + test3 + test4) / 4
        highest = max(test1, test2, test3, test4)
        lowest = min(test1, test2, test3, test4)
        improvement = test4 - test1
        print("\nAll scores valid and no suspicious patterns detected.")
        print(f"Average score: {average:.2f}")
        print(f"Highest score: {highest}")
        print(f"Lowest score: {lowest}")
        print(f"Improvement from Test 1 to Test 4: {improvement}")
    else:
        print("\nInvalid scores or suspicious patterns detected.")
        if not valid_range:
            print("Error: One or more scores are out of the valid range (0-100).")
        if huge_jump:
            print("Warning: Suspicious large jump detected between tests.")
        if all_identical:
            print("Warning: All test scores are identical, which is unusual.")
def Event_Scheduler():
    print("=== EVENT SCHEDULING SYSTEM ===")
    # Event 1
    print("\nEVENT 1 DETAILS:")
    event1_name = input("Event name: ")
    event1_day = input("Day (Mon-Sun): ").lower()[:3] # First 3 letters
    event1_start = float(input("Start time (0-24): "))
    event1_end = float(input("End time (0-24): "))
    # Event 2
    print("\nEVENT 2 DETAILS:")
    event2_name = input("Event name: ")
    event2_day = input("Day (Mon-Sun): ").lower()[:3]
    event2_start = float(input("Start time (0-24): "))
    event2_end = float(input("End time (0-24): "))
    # YOUR CODE HERE
    # 1. Validate times are in range 0-24
    # 2. Validate end time > start time for each event
    # 3. Check for conflicts using complex conditions
    # 4. Calculate gap between events if same day
    # 5. Check for early/late scheduling issues
    # Valid days
    valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    # Validation using chained comparisons
    event1_valid = (0 <= event1_start < 24) and (0 < event1_end <= 24) and (event1_end > event1_start) and (event1_day in valid_days)
    event2_valid = (0 <= event2_start < 24) and (0 < event2_end <= 24) and (event2_end > event2_start) and (event2_day in valid_days)
    # Check for conflicts
    same_day = event1_day == event2_day
    overlap = event1_end > event2_start and event2_end > event1_start
    conflict = same_day and overlap
    # Calculate gap if same day and no conflict
    gap = None
    if same_day and not conflict:
        if event1_end <= event2_start:
            gap = event2_start - event1_end
        elif event2_end <= event1_start:
            gap = event1_start - event2_end
    # Early/Late scheduling issues
    early_event1 = event1_start < 8
    late_event1 = event1_end > 20
    early_event2 = event2_start < 8
    late_event2 = event2_end > 20
    # Output results
    print()
    if not event1_valid:
        print(f"Error: Event 1 '{event1_name}' has invalid time or day.")
    if not event2_valid:
        print(f"Error: Event 2 '{event2_name}' has invalid time or day.")
    if event1_valid and event2_valid:
        if conflict:
            print(f"Conflict detected: '{event1_name}' and '{event2_name}' overlap on {event1_day.title()}.")
        else:
            print(f"No conflict between '{event1_name}' and '{event2_name}'.")
            if gap is not None:
                print(f"Time gap between events: {gap} hours.")
            else:
                print("Events are on different days, no gap calculation.")
        if early_event1:
            print(f"Warning: Event 1 '{event1_name}' starts early at {event1_start}h.")
        if late_event1:
            print(f"Warning: Event 1 '{event1_name}' ends late at {event1_end}h.")
        if early_event2:
            print(f"Warning: Event 2 '{event2_name}' starts early at {event2_start}h.")
        if late_event2:
            print(f"Warning: Event 2 '{event2_name}' ends late at {event2_end}h.")

# PROGRAM 5: Retail Discount Calculator
def Discount_Calculator():
    print("=== RETAIL DISCOUNT CALCULATOR ===")
    # Get inputs
    price = float(input("Item price: $"))
    quantity = int(input("Quantity: "))
    customer_type = input("Customer type (regular/member/vip/employee): ").lower()
    day = input("Day of week: ").lower()
    coupon = input("Coupon code (or 'none'): ").upper()
    # YOUR CODE HERE
    # Calculate each discount using conditional expressions
    # Apply discounts in order (multiplicative, not additive)
    # Check maximum discount rule
    # Show complete breakdown
    # Calculate subtotal
    subtotal = price * quantity
    # Bulk discount (use conditional expression)
    bulk_rate = 0.10 if quantity >= 10 else 0.05 if quantity >= 5 else 0
    bulk_discount = subtotal * bulk_rate
    # Continue with other discounts...  
    member_rate = 0.05 if customer_type == "member" else 0.10 if customer_type == "vip" else 0.30 if customer_type == "employee" else 0
    member_discount = (subtotal - bulk_discount) * member_rate  
    day_rate = 0.10 if day == "wednesday" else 0.05 if day == "saturday" else 0
    day_discount = (subtotal - bulk_discount - member_discount) * day_rate
    coupon_rate = 0.10 if coupon == "SAVE10" else 0.15 if coupon == "SAVE15" else 0
    coupon_discount = (subtotal - bulk_discount - member_discount - day_discount) * coupon_rate
    # Total discount
    total_discount = bulk_discount + member_discount + day_discount + coupon_discount
    # Final total
    final_total = subtotal - total_discount
    # Output breakdown
    print("\n--- DISCOUNT BREAKDOWN ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Bulk discount ({bulk_rate*100}%): -${bulk_discount:.2f}")
    print(f"Member discount ({member_rate*100}%): -${member_discount:.2f}")
    print(f"Day discount ({day_rate*100}%): -${day_discount:.2f}")
    print(f"Coupon discount ({coupon_rate*100}%): -${coupon_discount:.2f}")
    print()
    print(f"Total discount: -${total_discount:.2f}")
    print()
    print(f"Final total: ${final_total:.2f}")
    
# Main program loop to select and run each program
running = True
while running == True:
    print("\n1: Smart Thermostat System\n2: Password Security Analyzer\n3: Student Grade Validator\n4: Event Scheduling System\n5: Retail Discount Calculator\n")
    programchoice = input("Enter program to run (1-5): ")
    if programchoice == "1":
        Smart_Thermostat()
    elif programchoice == "2":
        Password_Security()
    elif programchoice == "3":
        Grade_Validator()
    elif programchoice == "4":
        Event_Scheduler()
    elif programchoice == "5":
        Discount_Calculator()
    else:
        print("Invalid program choice.")
    print()
    print("Would you like to run another program?")
    again = input("Enter 'y' to run again, anything else to quit: ").lower()
    if again != 'y':
        running = False
        print("Exiting program. Goodbye!")
    