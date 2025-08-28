# exercise3.py
# Arithmetic Operations Lab
# Cody Burton
# 8/25/2025

# Test numbers
a = 17
b = 5
c = 2.5

print("Test Values:")
print(f"a = {a}, b = {b}, c = {c}")
print("-" * 30)

# TODO: Perform each operation and observe results
# Addition
add_result = a + b
print(f"{a} + {b} = {add_result}")

# Subtraction
sub_result = a - c
print(f"{a} - {c} = {sub_result}")

# Multiplication
mult_result = b * c
print(f"{b} * {c} = {mult_result}")

# Division (/) - note the type!
div_result = b / b
print(f"{b} / {b} = {div_result} (Type: {type(div_result)})")

# Integer Division (//)
int_div_result = a // b
print(f"{a} // {b} = {int_div_result}")

# Modulo (%)
mod_result = a % b
print(f"{a} % {b} = {mod_result}")

# Exponentiation (**)
exp_result = a ** a
print(f"{a} ** {a} = {exp_result}")

print("-" * 30)
# TODO: Mixed type operations
print("Mixed Type Operations:")
# What happens with int + float?
mixed1 = a + c
print(f"{a} + {c} = {mixed1} (Type: {type(mixed1)})")
# Try more mixed operations
mixed2 = b * c
print(f"{b} * {c} = {mixed2} (Type: {type(mixed2)})")

mixed3 = c / a
print(f"{c} / {a} = {mixed3} (Type: {type(mixed3)})")

mixed4 = c // b
print(f"{c} // {b} = {mixed4} (Type: {type(mixed4)})")

# TODO: Special cases to explore
print("\nSpecial Cases:")
# Large numbers
big = 10 ** 100 # 10 to the power of 100
print(f"10^100 = {big}")
print(f"Python handles large numbers: {type(big)}")
# Negative division
neg_result = -17 // 5
print(f"-17 // 5 = {neg_result} (Note: rounds DOWN)")
# Division by zero (uncomment to see error)
# error_result = 10 / 0

# Test Your Understanding
# 1. What is the difference between / and // in Python?
#    / performs floating-point division, while // performs integer division
# 2. What type does / always return?
#    It always returns a float.
# 3. How does Python handle very large numbers?
#    Python can handle large numbers, as long as there is enough memory.
# 4. What happens with negative integer division?
#    It rounds down to the nearest whole number.