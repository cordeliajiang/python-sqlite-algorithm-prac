# variable n is declared to store user input
# input is converted to integer
n = int(input("Enter a positive number: "))


# print a diamond shape with 2*n-1 rows
# if input n = 3, 2*n-1 = 5
rows = 2*n-1


# structuring the upper half of the diamond
# as i starts from 0, to have 3 rows, n-1
# if input n = 3, n-1 = 2, rows = 5, i goes up to 2 (0, 1, 2)
for i in range(rows - (n-1)):

    # n-1-i, initially the first sub-loop will have 2 spaces
    # i determining the amount of spaces to add before "x"
    # as sub-loop number increases
    # 1+i*2, 1 is the base value, as the first sub-loop will have one "x"
    # each loop will add (loop num * 2) on top of the initial 1
    print(" " * ((n-1)-i) + "x" * (1+(i*2)))


# structuring the lower half of the diamond
# to have 2 rows, rows - n
# if input n = 3, rows = 5, i goes up to 1 (0, 1)
for j in range(rows - n):

    # initially the first sub-loop will have 1 space, hence n-(n-1)
    # j determining the amount of spaces to add before "x"
    # as sub-loop number increases
    # 2*n-3 is the base value, as the first sub-loop will have three "x"
    # each loop will add (loop num * 2) on top of the base value 2*n-3
    print(" " * (n-(n-1)+j) + "x" * ((2*n-3)-j*2))
