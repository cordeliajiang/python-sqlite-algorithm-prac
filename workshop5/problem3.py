# problem 3, 22/04/21, Cordelia Jiang
# write a function to calculate the numbers of days from starting year to ending year inclusive
# check for leap year

def number_of_days():
    year_input1 = int(input("Year 1: "))  # starting year
    year_input2 = int(input("Year 2: "))  # ending year
    days = 0

    if year_input1 > year_input2:
        print("Year 1 number should only be smaller than or equals to year 2")

    # check whether a year is a leap year
    # count from start year to end year
    while year_input1 <= year_input2:
        if year_input1 % 4 == 0 and year_input1 % 100 != 0 or year_input1 % 400 == 0:
            days += 366
        else:
            days += 365

        year_input1 += 1

    print("Number of days: ", days)


number_of_days()
