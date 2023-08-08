# problem 1, 21/04/21, Cordelia Jiang
# asking for string input, stop asking until a string starts with A is entered
# print shortest string, with single quotes around the string

stringInput = input("Enter a string: ")
shortestStringInput = stringInput


inputs = [] # string array
inputs.append(stringInput)  # initialise inputs array with new item stringInput


# loop that test for the sentinel A
while not stringInput.startswith("A"):
    stringInput = input("Enter a string: ")
    inputs.append(stringInput)  # push string input into inputs array

    # for each input in inputs array, if current input length is shorter
    # than default shortest, then current looped input is the shortest
    for i in inputs:
        if len(i) <= len(shortestStringInput):
            shortestStringInput = i

print("Shortest was: ", "'", shortestStringInput, "'")
