# Define encryption
def encrypt():
  new_char = ""
  for letter in text:
    if letter in alphabet: #check whether the letter is in the list, if no, just add respective symbol/space
      position = alphabet.index(letter) + shift
      if position < len(alphabet):
        new_char += alphabet[position]
      else:
        #for index number greater than 26, retrieve the value starting from 'a' again
        new_char += alphabet[position - 26]
    else:
      new_char += letter
  print(new_char)

# Define decryption
def decrypt():
  new_char = ""
  for letter in text:
    if letter in alphabet: #check whether the letter is in the list
      position = alphabet.index(letter) - shift
      new_char += alphabet[position]
    else:
      new_char += " "
  print(new_char)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
  encrypt()
elif direction == "decode":
  decrypt()
else:
  print('WARNING!!! Please type only "encode" or "decode" ONLY!')