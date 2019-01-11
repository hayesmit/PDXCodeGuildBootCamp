#lab13-ROT_Cipher.py
import string
rotation = int(input("0-26 how many rotations do you want the cypher to rotate? >>"))
alpha = string.ascii_lowercase
listed_alpha = list(alpha)
cipher = alpha[rotation: 26]+alpha[:rotation]
print(cipher)
my_indexes = []
encript_decript = input("do you want to encrypt or decrypt something? >>  ")
new_cipher = []
deciphered = []
#look at unikas examples, you can look up a letter and translate it in one move instead of puting it into a list
#that you have to call again later, you can add the cypher amount then modulous 26 to loop back to the start of the
#alphabet.

# finds all indexes of the word form a-z and makes the list of locations
def find_indexes(word):
    word = list(word)
    for i in word:
        my_indexes.append(listed_alpha.index(i))


#takes the indeses from a-z and plug the indexes into the cipher list
def encode(locations):
    for i in locations:
        new_cipher.append(cipher[i])


#takes the scrable and finds locations
def find_scrambled_locations(scramble):
    original_cipher = list(scramble)
    for i in original_cipher:
        my_indexes.append(cipher.index(i))


def decode(scramble):
    for i in scramble:
        deciphered.append(listed_alpha[i])


if encript_decript == "encrypt":
    realWord = input("what do you want to encrypt? >>  ")
    find_indexes(realWord)
    encode(my_indexes)
    encoded = ''.join(new_cipher)
    print(encoded)
elif encript_decript == "decrypt":
    jumble = input("what would you like to decipher? >>  ")
    find_scrambled_locations(jumble)
    decode(my_indexes)
    decoded = ''.join(deciphered)
    print(decoded)
