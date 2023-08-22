# add your code here
message = "python is fun!"
shift = 5

LAST_CHAR_CODE = 122
CHAR_RANGE = 26


def caesar_shift(message, shift):
    # Result placeholder.
    result = "The encrypted sentence is: "

    # Go through each of the letters in the message.
    for char in message.lower():
        if char.isalpha():
            # Convert character to the ASCII code.
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
    
            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    print(result)



user_message = input("Please enter a sentence: ")
caesar_shift(user_message, shift)
