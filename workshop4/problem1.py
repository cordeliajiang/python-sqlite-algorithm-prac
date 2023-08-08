# reads whole numbers typed by user until a zero is entered
# convert input into integer
numInput = int(input("Enter a number: "))


# declare variable positiveNumCount to hold for count of positive numbers
# initiating positiveNumCount to 0
positiveNumCount = 0


# while loop will terminate when numInput = 0
# only add 1 to positiveNumCount if numInput is bigger than 0
while numInput != 0:
    if numInput > 0:
        positiveNumCount += 1
    # read value to check whether the inputted number is sentinel
    numInput = int(input("Enter a number: "))


# print the number of positive numbers that were entered
print(positiveNumCount, "positive numbers were entered.")
