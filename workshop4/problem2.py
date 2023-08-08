# variable n is declared to store user input for fibonacci numbers
# input is converted to integer
n = int(input("Enter a positive number: "))


# fibonacci numbers starting from 0 and 1
f1 = 0
f2 = 1


# f3 is declared to take in sum of f1 and f2, as each fibonacci number
# is sum of the two proceeding numbers
f3 = f1 + f2


# line changing variable, initialized to 2,
# counter start from 2, as f1 and f2 are not printed within the for loop
# which the counter variable is used in
counter = 2


# user input n cannot be 0, print f1 if n is 0, print f2 if n is 1
if n < 0:
    print("invalid input")
elif n == 0:
    print(f1)
elif n == 1:
    print(f2)

# else, print f1, f2, and give a space to the end of each argument
# within this print function
else:
    print(f1, f2, end=" ")

    # n-2, as f1 and f2 are not printed within this for loop
    for i in range(n-2):
        # for each loop, fibonacci number will be formed based on the
        # the sum of the two proceeding number f1 and f2
        f3 = f1 + f2
        # for each loop, f1 in previous loop will become f2,
        # and f2 will be become f3
        f1 = f2
        f2 = f3
        # add 1 to counter, the line changing variable
        counter += 1

        # at most, 4 numbers can be displayed in a row
        # if there is less than 4 numbers displayed in a row, give a
        # space to the end of each argument within this print function
        if counter < 4:
            print(f3, end=" ")

        # print next number on a new line if there are 4 numbers in
        # a row
        else:
            print(f3, end="\n")

            # reset counter, the line changing variable to 0, and go
            # onto the next loop
            counter = 0
