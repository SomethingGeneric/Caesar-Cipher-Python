
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
        print(f"{text} with a shift of {str(i)}")
        if input("Is it readable? (y/N): ") == "y":
            break

while True:
    print(
        'Welcome to my Word..\n [*] Press 1 for Encryption \n [*] Press 0 for Decryption \n [*] Press 2 for brute decrypt \n [*] Press 01 to exit.. ')
    print('Tip ---> Encryption/Decryption with shift value of your choice ! ')
    choice = input('Insert Here : ')
    if choice.isdigit():
        if choice == '1':
            sen = input('Insert the plaintext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your ciphertext ---> {Encryption(sen, key)}')
            print(50 * '-')
            print('Special symbols (!,# etc and numbers) are deleted..')
            con = input('Shall we continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
        elif choice == '0':
            csen = input('Insert the ciphertext : ')
            key = int(input('Insert shift value(Only integer values) : '))
            print(50 * '-')
            print(f'Your plaintext ---> {Decryption(csen, key)}')
            print(50 * '-')
            print('Special symbols (!,# etc and numbers) are deleted..')
            con = input('Shall we continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
        elif choice == "2":
            enctext = input("Text: ")
            BruteDecrypt(enctext) 
            con = input('Shall we continue ? [Any Key/no]')
            if con == 'no':
                print('Exiting..')
                break
            else:
                pass
        elif choice == '01':
            print('Exiting..')
            break
        else:
            print('Exception error .. \n'
                  'Please insert 0 or 1 ')
