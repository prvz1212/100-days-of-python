import alphabet as al
import art

print(art.logo)


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in al.alphabet:
            output_text += letter
        else:
            shifted_position = al.alphabet.index(letter) + shift_amount
            shifted_position %= len(al.alphabet)
            output_text += al.alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


want_to_play = False
while not want_to_play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    again = input("Want to do it again ? type 'y' for YES or 'n' for NO: ").lower()
    if again == 'n':
        want_to_play = True
    elif again == 'y':
        want_to_play = False
    else:
        print("Invalid statement")
        want_to_play = True
