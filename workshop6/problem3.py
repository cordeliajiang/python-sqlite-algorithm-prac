# problem3, 28/04/21, Cordelia Jiang
# write a function to print True if all the g’s in the given string are happy, otherwise,
# print False. A lowercase ’g’ in a string means ”happy” if there is neighbouring g's.
stringInput = input("String: ")


# checks position for 'g' and its neighbouring g's, happyBool is True if there is adjacent 'g'
# in a string
def happy_gs(stringInput):
    for i in range(len(stringInput)):
        if stringInput[i] == "g" and stringInput[i - 1] == "g":
            happyBool = True
            break
        elif stringInput[i] == "g" and stringInput[i + 1] == "g":
            happyBool = True
            break
        else:
            happyBool = False
            continue
    if len(stringInput) == 1 and stringInput[0] == "g":
        happyBool = False
    print("Happy?:", happyBool)


happy_gs(stringInput)
