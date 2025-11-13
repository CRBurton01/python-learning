
# Problem 1: 
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    # Formula: F = C * 9/5 + 32
    # Your code here
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # Formula: C = (F - 32) * 5/9
    # Your code here
    celsius = (fahrenheit - 32) * 5/9
    return celsius
def temperature_report(temp, scale="C"):
    """
    Print temperature in both scales.
    Parameters:
    temp: temperature value
    scale: "C" for Celsius or "F" for Fahrenheit (default "C")
    """
    # Your code here
    # If scale is "C", show temp in C and converted to F
    # If scale is "F", show temp in F and converted to C
    if scale == "C":
        fahrenheit = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit:.2f}°F")
    elif scale == "F":
        celsius = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {celsius:.2f}°C")
    else:
        print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")
        
def calculate_weighted_grade(homework, midterm, final, hw_weight=0.3, mid_weight=0.3, final_weight=0.4):
    """
    Calculate weighted grade.
    Parameters:
    homework: homework average (0-100)
    midterm: midterm score (0-100)
    final: final exam score (0-100)
    hw_weight: homework weight (default 0.3)
    mid_weight: midterm weight (default 0.3)
    final_weight: final weight (default 0.4)
    Returns:
    Weighted average as float
    """
    # Your code here
    weighted_average = (homework * hw_weight) + (midterm * mid_weight) + (final * final_weight)
    return weighted_average

def get_letter_grade(score):
    """Convert numeric score to letter grade"""
    # A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
    # Your code here
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

#Problem 2: Grade Report
def print_grade_report(name, hw, mid, final):
    """Print complete grade report for a student"""
    # Use the other functions to calculate and display:
    # - Student name
    # - Individual scores
    # - Weighted average
    # - Letter grade
    # Your code here
    weighted_avg = calculate_weighted_grade(hw, mid, final)
    letter_grade = get_letter_grade(weighted_avg)
    print(f"Grade Report for {name}:")
    print(f"  Homework: {hw}")
    print(f"  Midterm: {mid}")
    print(f"  Final: {final}")
    print(f"  Weighted Average: {weighted_avg:.2f}")
    print(f"  Letter Grade: {letter_grade}")

#Problem 3: Scope Challenge
# BROKEN CODE - FIX THE SCOPE ISSUES
total_points = 0
bonus_multiplier = 1.1
def add_score(points):
    """Add points to total score"""
    global total_points # Global is needed to modify the global variable
    total_points = total_points + points
    return total_points
def apply_bonus():
    """Apply bonus multiplier to total"""
    global total_points  # Global is needed to modify the global variable here too
    total_points = total_points * bonus_multiplier
    return total_points
def get_final_score():
    """Get the final score"""
    global total_points # Global is needed to access the global variable here as well
    final = total_points
    return final
def reset_score():
    """Reset the total points to zero"""
    global total_points
    total_points = 0

# Main Program Picker
def main():
    while True:
        # Program picker
        print("Choose a program to run:")
        print("1: Temperature Conversion")
        print("2: Grade Report")
        print("3: Weighted Grade Calculation")
        print("Q: Quit")
        print()
        choice = input("Enter the number of the program to run: ")
        if choice == "1":
            # Temperature Conversion Program
            temp = float(input("Enter the temperature value: "))
            scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ").upper()
            temperature_report(temp, scale)
        elif choice == "2":
            # Grade Report Program
            name = input("Enter student name: ")
            hw = float(input("Enter homework average (0-100): "))
            mid = float(input("Enter midterm score (0-100): "))
            final = float(input("Enter final exam score (0-100): "))
            print_grade_report(name, hw, mid, final)
        elif choice == "3":
            # Scope Challenge Program
            # Test your fixes:
            add_score(100)
            add_score(50)
            apply_bonus()
            print(f"Final score: {get_final_score()}") # Should print 165.0
            reset_score()
        elif choice.upper() == "Q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()