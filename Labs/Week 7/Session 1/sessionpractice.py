# Activity 1
# Define variables of different types
a = 42
b = "Python"
c = [1, 2, 3]
d = 3.14
e = True
greeting = "Good "
og = [10, 20, 30]
copy1 = og
copy2 = og

# Print variable locations in memory
locA=id(a)
locB=id(b)
locC=id(c)
locD=id(d)
locE=id(e)
locG=id(greeting)
locOg=id(og)
locC1=id(copy1)
locC2=id(copy2)

print("Initial memory locations:")
print(locA)
print(locB)
print(locC)
print(locD)
print(locE)
print(locG)
print(locOg)
print(locC1)
print(locC2)
print()

# Change variable values
a = 67
b = "Programming"
c.append(4)
d = 2.71
e = False
greeting += "Morning"
copy1[1] = 200
copy2[2] = 300

# Check if variables are immuatble/mutable
newLocA=id(a)
newLocB=id(b)
newLocC=id(c)
newLocD=id(d)
newLocE=id(e)
newLocG=id(greeting)
newLocC1=id(copy1)
newLocC2=id(copy2)

print("New memory locations after changes:")
print(newLocA)
print(newLocB)
print(newLocC)
print(newLocD)
print(newLocE)
print(newLocG)
print(newLocC1)
print(newLocC2)
print()

# Print results of memory location changes
print("Memory location changes:")
print("a changed:", locA != newLocA)
print("b changed:", locB != newLocB)
print("c changed:", locC != newLocC)
print("d changed:", locD != newLocD)
print("e changed:", locE != newLocE)
print("greeting changed:", locG != newLocG)
print("copy1 changed:", locC1 != newLocC1)
print("copy2 changed:", locC2 != newLocC2)
print("Values of og, copy1, and copy2:", og, copy1, copy2)

# Activity 2
'''Without using loops: 
1. Create a list of the first 10 even numbers (range and list)
2. Create a checkerboard pattern [0, 1, 0, 1, 0, 1... ]
3. Create a list that contains 3 empty lists
4. Create a list from the string "1,2,3" that gives [1, 2, 3]
    (Use split() then convert strings to int manually)'''

evenNums = list(range(0, 20, +2))
print(evenNums)
checkerboard = [
    [[0, 1] * 5,
    [1, 0] * 5] * 2,
    [0, 1] *5
]
print(checkerboard)

strnumbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

movies = ["Star Wars 4", "The Hunger Games", "Twilight", "Sonic 2"]
ratings = [5, 4, 0, 2]

for r in movies:
    print(f"{r} - {ratings[movies.index(r)]} Stars {'*' * ratings[movies.index(r)]}")
    

