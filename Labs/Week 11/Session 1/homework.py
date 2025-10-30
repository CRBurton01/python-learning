# Homework 10
# Cody Burton
# Program imports

# Problem 1: Multiplication Table
def MultiplicationTable():
    print("Problem 1: Multiplication Table")
    size = 0
    while size == 0:
        size = int(input("Enter the size of the multiplication table (1-12): "))
        if size < 1 or size > 12:
            print("Invalid size. Please enter a number between 1 and 12.")
            size = 0
    print()
    print(" " * 5, end="")
    for i in range(1, size + 1):
        print(f"{i:4}", end="")
    print()
    print("    +" + "----" * size)
    for i in range(1, size + 1):
        print(f"{i:3}|", end="")
        for j in range(1, size + 1):
            print(f"{i * j:4}", end="")
        print()
        
# Problem 2: Pattern Detective
def PatternDetective():
    print("Problem 2: Pattern Detective")
    numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]

    # Single-pass compute initial metrics
    found = None
    even = lt25 = lt50 = lt75 = lt100 = total_div3 = 0
    for idx, n in enumerate(numbers):
        if found is None and n > 75:
            found = (n, idx)
        if n % 2 == 0:
            even += 1
        if n <= 25:
            lt25 += 1
        elif n <= 50:
            lt50 += 1
        elif n <= 75:
            lt75 += 1
        else:
            lt100 += 1
        if n % 3 == 0:
            total_div3 += n

    print("Looking for number greater than 75...")
    if found:
        print(f"Found {found[0]} at index {found[1]}!\n")
    else:
        print("No number greater than 75 found.\n")

    print("Looking for even numbers...")
    print(f"Total even numbers found: {even}\n")

    print("Sorting numbers into ranges...")
    print(f"Numbers <= 25: {lt25}")
    print(f"Numbers > 25 and <= 50: {lt50}")
    print(f"Numbers > 50 and <= 75: {lt75}")
    print(f"Numbers > 75: {lt100}\n")

    print("Adding numbers divisible by 3...")
    print(f"Total sum of numbers divisible by 3: {total_div3}\n")

    # Allow user to add numbers; update metrics incrementally
    while True:
        try:
            add = int(input("Enter a number to add to the list (-1 to stop): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if add == -1:
            break
        numbers.append(add)
        print(f"Added {add} to the list.")
        
    print(f"Final list of numbers (new length {len(numbers)}):")
    print(numbers)
    
# Main program loop (need to implement other problems)
def main():
    running = True
    while running:
        print()
        print("Select a problem to run:")
        print("1. Multiplication Table")
        print("2. Pattern Detective")
        print("3. Exit")
        choice = input("Enter a problem # to run: ")
        print()
        if choice == '1':
            MultiplicationTable()
        elif choice == '2':
            PatternDetective()
        elif choice == '3':
            print("Exiting the program. Thank you!")
            running = False
        else:
            print("Invalid choice. Please select a valid problem number.")
if __name__ == "__main__":
    main()