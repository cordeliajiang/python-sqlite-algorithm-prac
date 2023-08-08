# problem 2, 21/04/21, Cordelia Jiang
# write a function that loop through characters in string input,
# replace digit in string to underline

def digit_to_underline():
    string_input = input("Input a string? ")

    for character in string_input:
        if character.isdigit():
            string_input = string_input.replace(character, "_")

    print("Output: ", string_input)


digit_to_underline()
