items = ["orange", "apple", "banana", "grape", "kiwi"]
prices = [0.50, 0.75, 0.30, 1.00, 1.50]
total = 0.0
subtotal = 0.0
for i in items:
    print(f"Item #{items.index(i)+1} - {i} - ${prices[items.index(i)]:.2f}")
    
itemselection = int(input("Select an item by number (1-5): "))
if itemselection < 1 or itemselection > 5:
    print("Invalid selection. Please select a number between 1 and 5: ")
else:
    quantity = int(input("Enter quantity: "))
    if quantity < 1:
        print("Invalid quantity. Please enter a positive integer.")
    else:
        if itemselection == 1:
            subtotal = prices[0] * quantity
            print(f"You selected {quantity} orange(s). Total cost: ${subtotal:.2f}")
        elif itemselection == 2:
            subtotal = prices[1] * quantity
            print(f"You selected {quantity} apple(s). Total cost: ${subtotal:.2f}")
        elif itemselection == 3:
            subtotal = prices[2] * quantity
            print(f"You selected {quantity} banana(s). Total cost: ${subtotal:.2f}")
        elif itemselection == 4:
            subtotal = prices[3] * quantity
            print(f"You selected {quantity} grape(s). Total cost: ${subtotal:.2f}")
        elif itemselection == 5:
            subtotal = prices[4] * quantity
            print(f"You selected {quantity} kiwi(s). Total cost: ${subtotal:.2f}")
    if quantity >= 10:
        discount = subtotal * 0.10
        total = subtotal - discount
        print(f"Bulk purchase discount applied! You saved: ${discount:.2f}")
        print(f"New total cost: ${total:.2f}")
    ismember = input("Are you a member? (yes/no): ").lower()
    if ismember == "yes":
        member_discount = total * 0.05
        total -= member_discount
        print(f"Membership discount applied! You saved: ${member_discount:.2f}")
        print(f"New total cost: ${total:.2f}")
    else:
        print("No membership discount applied.")
    # Print final total
    print(f"Subtotal: ${subtotal:.2f}")
    tax = subtotal * 0.08
    print(f"Tax (8%): ${tax:.2f}")
    total += tax
    print(f"Final Total: ${total:.2f}")
print()

#Health Advisor
print("=== Health Advisor ===")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in pounds): "))
height = float(input("Enter your height (in inches): "))
exercise = int(input("How many days per week do you exercise? "))
sleep = int(input("How many hours of sleep do you get per night? "))
water = int(input("How many glasses of water do you drink daily? "))
advice = ""
healthscore = 0

bmi = (weight / (height ** 2)) * 703
if bmi < 18.5:
    advice += "You are underweight. Consider a balanced diet to gain weight.\n"
    healthscore += 15
elif 18.5 <= bmi < 24.9:
    advice += "You have a normal weight. Keep up the good work!\n"
    healthscore += 25
elif 25 <= bmi < 29.9:
    advice += "You are overweight. Consider a healthy diet and regular exercise.\n"
    healthscore += 10
elif bmi >= 30:
    advice += "You are obese. It's important to consult a healthcare provider for guidance.\n"

if age < 18:
    if exercise < 1:
        advice += "Try to exercise at least 1 hour daily.\n"
    else:
        healthscore += 25
    if sleep < 8:
        advice += "Aim for 8-10 hours of sleep per night.\n"
    else:
        healthscore += 25
    if water < 2:
        advice += "Drink at least 2 glasses of water daily.\n"
    else:
        healthscore += 25
elif 18 <= age < 65:
    if exercise < 3:
        advice += "Try to exercise at least 30 minutes, 3 times a week.\n"
    else:
        healthscore += 25
    if sleep < 7:
        advice += "Aim for 7-9 hours of sleep per night.\n"
    else:
        healthscore += 25
    if water < 4:
        advice += "Drink at least 4 glasses of water daily.\n"
    else:
        healthscore += 25
elif age >= 65:
    if exercise < 2:
        advice += "Try to exercise at least 30 minutes, 2 times a week.\n"
    else:
        healthscore += 25
    if sleep < 7:
        advice += "Aim for 7-8 hours of sleep per night.\n"
    else:
        healthscore += 25
    if water < 6:
        advice += "Drink at least 6 glasses of water daily.\n"
    else:
        healthscore += 25
print(f"Your health score is: {healthscore}/100")
print(f"Your BMI is: {bmi:.2f}")
print("Health Advice:")
print(advice)
print()

# Email Form Vaildation
print("=== Email Form Validation ===")
name = input("Enter your name: ")
email = input("Enter your email: ")
subject = input("Enter the subject: ")
message = input("Enter your message: ")

if len(name) < 2:
    print("Error: Name must be at least 2 characters long.")
elif len(name) > 50:
    print("Error: Name must be no more than 50 characters long.")

if "@" not in email or "." not in email:
    print("Error: Email must contain '@' and '.' characters.")
elif email.count("@") != 1:
    print("Error: Email must contain exactly one '@' character.")
elif email.startswith("@") or email.endswith("@"):
    print("Error: '@' cannot be the first or last character in the email.")
elif email.startswith(".") or email.endswith("."):
    print("Error: '.' cannot be the first or last character in the email.")
elif email.index(".") < email.index("@"):
    print("Error: '.' must come after '@' in the email.")
elif " " in email:
    print("Error: Email cannot contain spaces.")
elif len(email) < 5 or len(email) > 100:
    print("Error: Email must be between 5 and 100 characters long.")
    
if len(subject) > 100:
    print("Error: Subject must be at most 100 characters long.")
if len(subject) == 0:
    print("Error: Subject cannot be empty.")
    
if len(message) > 500:
    print("Error: Message must be at most 500 characters long.")
if len(message) < 10:
    print("Error: Message must be at least 10 characters long.")
print()

# Credit Card Validator
print("=== Credit Card Validator ===")
card_number = input("Enter your credit card number (no spaces or dashes): ")
if not card_number.isdigit():
    print("Error: Credit card number must contain only digits.")
elif len(card_number) != 16:
    print("Error: Credit card number must be exactly 16 digits long.")
elif card_number[0] not in ['4', '5', '6']:
    print("Error: Credit card number must start with 4, 5, or 6.")
elif card_number[0] in ['4', '5', '6']:
    if card_number[0] == '4':
        print("Credit card type: Visa")
    elif card_number[0] == '5':
        print("Credit card type: MasterCard")
    elif card_number[0] == '6':
        print("Credit card type: Discover")
else:
    has_consecutive = False
    for i in range(len(card_number) - 1):
        if card_number[i] == card_number[i + 1]:
            has_consecutive = True
            break
    if has_consecutive:
        print("Error: Credit card number cannot have consecutive repeated digits.")
    else:
        print("Credit card number is valid.")
expdate = input("Enter expiration date (MM/YY): ")
if len(expdate) != 5 or expdate[2] != '/' or not expdate[:2].isdigit() or not expdate[3:].isdigit():
    print("Error: Expiration date must be in MM/YY format.")
else:
    month = int(expdate[:2])
    year = int(expdate[3:]) + 2000
    if month < 1 or month > 12:
        print("Error: Expiration month must be between 01 and 12.")
    else:
        from datetime import datetime
        current_year = datetime.now().year
        current_month = datetime.now().month
        if year < current_year or (year == current_year and month < current_month):
            print("Error: Credit card is expired.")
        else:
            print("Credit card expiration date is valid.")
cvv = input("Enter CVV (3 digits): ")
if len(cvv) != 3 or not cvv.isdigit():
    print("Error: CVV must be exactly 3 digits.")

cardholder_name = input("Enter cardholder name: ")
for n in cardholder_name:
    if not (n.isalpha() or n.isspace()):
        print("Error: Cardholder name must contain only letters and spaces.")
        break
if len(cardholder_name) < 2 or len(cardholder_name) > 50:
    print("Error: Cardholder name must be between 2 and 50 characters long.")
zipcode = input("Enter billing zip code (5 digits): ")
if len(zipcode) != 5 or not zipcode.isdigit():
    print("Error: Zip code must be exactly 5 digits.")
print()

