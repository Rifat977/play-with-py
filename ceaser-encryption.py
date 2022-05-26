import string

plain_text = input("Enter the text: ")

shift = 21

alphabet = string.ascii_lowercase

shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)
