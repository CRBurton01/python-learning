#Simple Fibonacci sequence generator
loops = input("Enter number of loops: ")
firstnum = 0
secondnum = 1
for i in range(int(loops)):
    print(firstnum)
    nextnum = firstnum + secondnum
    firstnum = secondnum
    secondnum = nextnum
#End of program

