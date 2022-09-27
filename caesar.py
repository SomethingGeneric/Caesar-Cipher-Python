import sys

from nostril import nonsense

def Encryption(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            ciphertext += ' '
        elif special.isalpha():
            ciphertext += chr((ord(new_special) + key_val - 97) % 26 + 97)

    return ciphertext


def Decryption(ciphertext, key_val):
    plaintext = ''
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        new_special = special.lower()
        if new_special == " ":
            plaintext += ' '
        elif special.isalpha():
            plaintext += chr((ord(new_special) - key_val - 97) % 26 + 97)
    return plaintext

def BruteDecrypt(ciphertext):
    for i in range(1,10000):
        text = Decryption(ciphertext,i)
        if not nonsense(text):
            print("Maybe: " + text)
            break

if sys.argv[1] == "enc":
    print(Encryption(sys.argv[2], int(sys.argv[3])))
elif sys.argv[1] == "dec":
    print(Decryption(sys.argv[2], int(sys.argv[3])))
elif sys.argv[1] == "magic":
    BruteDecrypt(sys.argv[2])