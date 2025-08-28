# exercise1.py
# Variable Type Demonstration
# Cody Burton
# 8/25/2025

# TODO: Create variables of each type
# Integer variable for your age
age = 18

# Float variable for your GPA (make one up if needed)
gpa = 3.8

# String variable for your name
name = "Cody"

# Boolean variable for whether you like Python
likes_python = True

# None variable for something not yet defined
future_job = None

# TODO: Print each variable and its type
print("Age:", age, "- Type:", type(age))
print("GPA:", gpa, "- Type:", type(gpa))
print("Name:", name, "- Type:", type(name))
print("Likes Python:", likes_python, "- Type:", type(likes_python))
print("Future Job:", future_job, "- Type:", type(future_job))

# TODO: Try these operations and observe what happens

# 1. Add 1 to age and print result
print("Age + 1:", age + 1)
# 2. Add 0.1 to GPA and print result
print("GPA + 0.1:", gpa + 0.1)
# 3. Multiply your name by 3 and print result
print("Name * 3:", name * 3)
# 4. What happens if you try: age + name? (Try it and comment out if it errors)
#print("Age + Name:", age + name) # This will raise a TypeError

#Test Your Understanding
# 1. What happens when you try to add an integer to a float?
#    The integet is converted and added as a float.
# 2. Can you multiply a string by a number? What does it do?
#    Yes, it will repeat the string that many times.
# 3. What errror do you get when you try to add a string to a number?
#    A TypeError for unsupported operand types.