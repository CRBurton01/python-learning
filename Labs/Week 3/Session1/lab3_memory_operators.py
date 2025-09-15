print("=== Memory Investigation ===")
# Create variables with small integers
a = 100
b = 100
print(f"a = {a}, memory address = {id(a)}")
print(f"b = {b}, memory address = {id(b)}")
print(f"a and b same object? {id(a) == id(b)}")
print()
# Create variables with large integers
c = 100000
d = 100000
print(f"c = {c}, memory address = {id(c)}")
print(f"d = {d}, memory address = {id(d)}")
print(f"c and d same object? {id(c) == id(d)}")
print()
# Create variables with strings
e = "Python"
f = "Python"
print(f"e = '{e}', memory address = {id(e)}")
print(f"f = '{f}', memory address = {id(f)}")
print(f"e and f same object? {id(e) == id(f)}")
print()
# Q1: Why do a and b share the same memory address?
# Your answer: Because small integers are chached by Python for memory efficiency

# Q2: Why might c and d have different memory addresses?
# Your answer: Because large integers are not cached like small integers

# Q3: What happens with string variables e and f?
# Your answer: Strings with the same value are interned by Python, so they share the same memory address

print("\n=== Variable References ===")
# Create a variable
original = 500
print(f"original = {original}, id = {id(original)}")
# Create a reference to the same object
reference = original
print(f"reference = original")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Same object? {id(original) == id(reference)}")
print()
# Now modify original
original = original + 100
print("After: original = original + 100")
print(f"original = {original}, id = {id(original)}")
print(f"reference = {reference}, id = {id(reference)}")
print(f"Still same object? {id(original) == id(reference)}")
print()
# YOUR TURN: Create your own example with strings
# Create a string variable
my_string = "Hello, World!"
print(f"my_string = '{my_string}', id = {id(my_string)}")
# Create a reference to it
my_reference = my_string
print(f"my_reference = my_string")
print(f"my_reference = '{my_reference}', id = {id(my_reference)}")
print(f"Same object? {id(my_string) == id(my_reference)}")
print()
# Modify the original using concatenation
my_string = my_string + " How are you?"
print("After: my_string = my_string + ' How are you?'")
print(f"my_string = '{my_string}', id = {id(my_string)}")
print(f"my_reference = '{my_reference}', id = {id(my_reference)}")
# Check if they still point to the same object
print(f"Still same object? {id(my_string) == id(my_reference)}")
print()

print("\n=== Operator Precedence - Predict First! ===")
# For each expression:
# 1. Write your prediction
# 2. Run the code
# 3. Explain why you got that result
# Example:
# Prediction: 14
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result}")
print("Explanation: Multiplication happens before addition\n")
# YOUR TURN - Predict before running:
# Prediction: 4
result1 = 10 - 2 * 3
print(f"10 - 2 * 3 = {result1}")
# Explanation: Multiplication happens first, then subtraction
# Prediction: 24
result2 = (10 - 2) * 3
print(f"(10 - 2) * 3 = {result2}")
# Explanation: The parentheses take priority in the operation order, so 10-2 is calculated first
# Prediction: 32
result3 = 2 ** 3 * 4
print(f"2 ** 3 * 4 = {result3}")
# Explanation:Exponentiation happens before multiplication
# Prediction: 4096
result4 = 2 ** (3 * 4)
print(f"2 ** (3 * 4) = {result4}")
# Explanation: The parentheses take priority, so 3*4 is calculated first
# Prediction: 50
result5 = 100 / 10 * 5
print(f"100 / 10 * 5 = {result5}")
# Explanation: Since division and multiplication have the same precedence, they are evaluated left to right
# Prediction: 2
result6 = 100 / (10 * 5)
print(f"100 / (10 * 5) = {result6}")
# Explanation: Parentheses take priority, so 10*5 is calculated first
print()

print("\n=== Fix the Expression with Parentheses ===")
# Each calculation is wrong. Add parentheses to fix it.
# Goal: Calculate the average of 10 and 20
wrong_avg = 10 + 20 / 2
print(f"Wrong average: {wrong_avg}")
# YOUR FIX:
fixed_avg = (10 + 20) / 2 
print(f"Fixed average: {fixed_avg}")
# Goal: Calculate 5% of 200
wrong_percent = 5 / 100 * 200
print(f"Wrong calculation: {wrong_percent}")
# YOUR FIX:
fixed_percent = (5 / 100) * 200
print(f"Fixed calculation: {fixed_percent}")
# Goal: Convert 75 minutes to hours (divide by 60)
wrong_hours = 75 / 60 * 60
print(f"Wrong hours: {wrong_hours}")
# YOUR FIX:
fixed_hours = 75 / 60
print(f"Fixed hours: {fixed_hours}")
print()

print("\n=== Understanding Division Operations ===")
# Regular division (/)
print("Regular division (/):")
print(f"17 / 5 = {17 / 5}")
print(f"20 / 4 = {20 / 4}")
print(f"Type of 20 / 4: {type(20 / 4)}")
print()
# Floor division (//)
print("Floor division (//):")
print(f"17 // 5 = {17 // 5}")
print(f"20 // 4 = {20 // 4}")
print(f"Type of 20 // 4: {type(20 // 4)}")
print()
# Modulo (%)
print("Modulo (%):")
print(f"17 % 5 = {17 % 5}")
print(f"20 % 4 = {20 % 4}")
print()
# YOUR TURN: Calculate these
numerator = 23
denominator = 7
regular_div = numerator / denominator 
floor_div = numerator // denominator
remainder = numerator % denominator
print(f"{numerator} / {denominator} = {regular_div}")
print(f"{numerator} // {denominator} = {floor_div}")
print(f"{numerator} % {denominator} = {remainder}")
# Verify: numerator should equal (floor_div * denominator) + remainder
verification = (floor_div * denominator) + remainder
print(f"Verification: {floor_div} * {denominator} + {remainder} = {verification}")
print()

