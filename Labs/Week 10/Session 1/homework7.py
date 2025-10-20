#Homework 7
#By Cody Burton

#Program imports
import random
import math

# Problem 1: Temperature Analysis
def TemperatureAnalysis():
    temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]
    sum_temp = 0
    count = 0
    max_temp = 0
    min_temp = 100
    above_72_count = 0
    for t in temperatures:
        sum_temp += t
        count += 1
        if t > max_temp:
            max_temp = t
        if t < min_temp:
            min_temp = t
        if t > 72:
            above_72_count += 1
        print(f"Temp #{count + 1}: {t}°F ({(t - 32) * 5 / 9:.2f} °C)")
    average_temp = sum_temp / count
    print()
    print("Temperature Analysis Results:")
    print(f"Average temperature: {average_temp:.2f}")
    print(f"Maximum temperature: {max_temp}")
    print(f"Minimum temperature: {min_temp}")
    print(f"Number of days above 72°F: {above_72_count}")

# Problem 2: Guessing Game
def GuessingGame():
    random_number = random.randint(1, 20)
    guesses = []
    attempts = 0
    guess = 0
    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 20.")
    print("You have five guesses to find the number.")
    while attempts < 5:
        guess = int(input(f"Enter guess #{attempts + 1}: "))
        guesses.append(guess)
        attempts += 1
        if guess < random_number:
            print("The number is higher! Try again.")
        elif guess > random_number:
            print("The number is lower! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempt(s).")
            if attempts == 1:
                print("Incredible! You guessed it on your first try!")
            elif attempts >= 3:
                print("Well done! You found the number, but it took a few tries.")
            elif attempts >= 5:
                print("Phew! You barely made it!")
            break
    if attempts == 5 and guess != random_number:
        print(f"Sorry, you've used all your attempts. The number was {random_number}.")
    print(f"Your guesses were: {guesses}")
    
# Problem 3: Grade Processor
def GradeProcessor():
    grades = [85, -10, 92, 150, 78, 0, 95, 88, -5, 100, 73, 200]
    invalid_grades = []
    invalid_counter = 0
    total_grades = len(grades)
    grades_sum = 0
    print("Grade Processing Results:")
    for grade in grades:
        if grade < 0 or grade > 100:
            print(f"Grade: {grade} is invalid.")
            invalid_grades.append(grades.pop(grades.index(grade)))
            invalid_counter += 1
    print()
    print("Valid Grades and Letter Grades:")
    for valid_grade in grades:
        print(f"Grade: {valid_grade}, Letter Grade: ", end="")
        if valid_grade >= 90:
            print("A")
        elif valid_grade >= 80:
            print("B")
        elif valid_grade >= 70:
            print("C")
        elif valid_grade >= 60:
            print("D")
        else:
            print("F")
        grades_sum += valid_grade
    print()
    print("Grade Distribution:")
    print(f"A: {sum(1 for g in grades if g >= 90)}")
    print(f"B: {sum(1 for g in grades if 80 <= g < 90)}")
    print(f"C: {sum(1 for g in grades if 70 <= g < 80)}")
    print(f"D: {sum(1 for g in grades if 60 <= g < 70)}")
    print(f"F: {sum(1 for g in grades if g < 60)}")
    print()
    print(f"Total Valid Grades Processed: {total_grades - invalid_counter}")
    print(f"Invalid Grades Encountered: {invalid_counter}")
    if invalid_counter > 0:
        print("Invalid Grades List:", invalid_grades)
    if total_grades - invalid_counter > 0:
        average_grade = grades_sum / (total_grades - invalid_counter)
        print(f"Average of Valid Grades: {average_grade:.2f}")

# Main function to select and run problems
def main():
    running = True
    while running:
        print()
        print("Select a problem to run:")
        print("1. Temperature Analysis")
        print("2. Guessing Game")
        print("3. Grade Processor")
        print("4. Exit")
        choice = input("Enter a problem # to run: ")
        print()
        if choice == '1':
            TemperatureAnalysis()
        elif choice == '2':
            GuessingGame()
        elif choice == '3':
            GradeProcessor()
        elif choice == '4':
            print("Exiting the program. Thank you!")
            running = False
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
if __name__ == "__main__":
    main()