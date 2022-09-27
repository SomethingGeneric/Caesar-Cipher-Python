import sys

from nostril import nonsense

def c_encrypt(plaintext, key_val):
    ciphertext = ''
    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()
        if new_special == " ":
            ciphertext += ' '
        elif special.isalpha():
            ciphertext += chr((ord(new_special) + key_val - 97) % 26 + 97)

    return ciphertext


def c_decrypt(ciphertext, key_val):
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
        text = c_decrypt(ciphertext,i)
        if not nonsense(text):
            print("Maybe: " + text)
            break

def multi_cypher(plaintext, key_sequence):
    this_pass = plaintext
    shifts = [*key_sequence]
    #print(str(shifts))
    for shift in shifts:
        this_pass = c_encrypt(this_pass, int(shift))
    return this_pass

def multi_cypher_decrypt(starter, key_sequence):
    this_pass = starter
    shifts = [*key_sequence]
    shifts.reverse()
    #print(str(shifts))
    for shift in shifts:
        this_pass = c_decrypt(this_pass, int(shift))
    return this_pass

if len(sys.argv) == 1:
    print("Usage:\n- enc <text> <shift>\n- dec <text> <shift>\n- multienc <text> <shift_seq>\n- multidec <text> <shift_seq>\n- magicdec <text>")
    sys.exit()

if sys.argv[1] == "enc":
    print(c_encrypt(sys.argv[2], int(sys.argv[3])))
elif sys.argv[1] == "dec":
    print(c_decrypt(sys.argv[2], int(sys.argv[3])))
elif sys.argv[1] == "multienc":
    print(multi_cypher(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "multidec":
    print(multi_cypher_decrypt(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "magicdec":
    BruteDecrypt(sys.argv[2])