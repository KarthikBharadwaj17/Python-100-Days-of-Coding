from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):

    cipher_text = " "    
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            if direction == "encode":
                new_index = index + shift

            elif direction == "decode":
                new_index = index - shift
            cipher_text += alphabet[new_index] 
        else:
            cipher_text += char
    print(f"The {direction} text is{cipher_text}.")

shift = shift % 26 
  
caesar(text=text, shift=shift, direction=direction)

user =  input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
should_continue = True
while(should_continue == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)

if user == "no":
    should_continue = False 
    print("Good Bye ")




