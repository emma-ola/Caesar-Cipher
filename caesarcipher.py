# Caesar Cipher
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
            , 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(input_text, shift_amount, cipher_direction):
    generated_text = ''
    if cipher_direction == 'encode' or cipher_direction == 'decode':
        for char in input_text:
            if char in alphabet:
                char_index = alphabet.index(char)
                if cipher_direction == 'encode':
                    new_cipher_index = char_index + shift_amount
                    new_cipher_char = alphabet[new_cipher_index]
                    generated_text += new_cipher_char
                elif cipher_direction == 'decode':
                    new_plain_text_index = char_index - shift_amount
                    new_plain_text_char = alphabet[new_plain_text_index]
                    generated_text += new_plain_text_char
            else:
                generated_text += char

        print(f"Here's the {method}d result: {generated_text}")
    else:
        print('That\'s an Invalid Choice\nType \'encode\' or \'decode\'')


print(logo)
should_continue = True
while should_continue:
    method = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # What this does is to divide the shift number entered by 26 and store the reminder as the shift number, so the
    # Shift number will always be in the range of our list.
    shift = shift % 26

    caesar(input_text=text, shift_amount=shift, cipher_direction=method)

    result = input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n')
    if result == 'no':
        should_continue = False
        print('Goodbye')
