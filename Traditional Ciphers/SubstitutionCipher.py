#  This is the module to encript and decript data using substitution cipher

import random as rd

KeyLetters = {
    'alphabets': 'abcdefghijklmnopqrstuvwxyz',
    'numbers': '0123456789',
    'symbols': '!@#$%^&*?\\/'
}

DataBase = {}

def Substitution_Cipher_Encrypt():
    EncriptText = input('Please Enter the text to Encrypt : ')
    UserName = input('Please give a name to store your decript key : ')
    
    RandomCodeGen_alphabets = rd.sample(KeyLetters['alphabets'] ,  len(KeyLetters['alphabets']))
    RandomCodeGen_numbers = rd.sample(KeyLetters['numbers'] ,  len(KeyLetters['numbers']))
    RandomCodeGen_symbols = rd.sample(KeyLetters['symbols'] ,  len(KeyLetters['symbols']))
    DataBase[UserName] = { 'alphabets':''.join(RandomCodeGen_alphabets) , 'numbers':''.join(RandomCodeGen_numbers) , 'symbols':''.join(RandomCodeGen_symbols)}
    
    EncriptedList = []

    for i in EncriptText:
        if i in KeyLetters['alphabets']:
            KeyIndexes= KeyLetters['alphabets'].find(i)
            EncriptedList.append(RandomCodeGen_alphabets[KeyIndexes])
        elif i in KeyLetters['numbers']:
            KeyIndexes = KeyLetters['numbers'].find(i)
            EncriptedList.append(RandomCodeGen_numbers[KeyIndexes])
        elif i in KeyLetters['symbols']:
            KeyIndexes = KeyLetters['symbols'].find(i)
            EncriptedList.append(RandomCodeGen_symbols[KeyIndexes])
        else:
            EncriptedList.append(' ')
    print(''.join(EncriptedList))
       

def Substitution_Cipher_Decrypt():
    DecryptName = input('please enter the decript username : ')
    DecryptText = input('Please enter the text to decript : ')
    if DecryptName in DataBase:
        userData = DataBase[DecryptName]

        DecriptedList = []
        for i in DecryptText:
            if i in KeyLetters['alphabets']:
                KeyIndexes= userData['alphabets'].find(i)
                DecriptedList.append(KeyLetters['alphabets'][KeyIndexes])
            elif i in KeyLetters['numbers']:
                KeyIndexes = userData['numbers'].find(i)
                DecriptedList.append(KeyLetters['numbers'][KeyIndexes])
            elif i in KeyLetters['symbols']:
                KeyIndexes = userData['symbols'].find(i)
                DecriptedList.append(KeyLetters['symbols'][KeyIndexes])
            else:        
                DecriptedList.append(' ')
        print(''.join(DecriptedList))

    else:
        print('User not present in the Database , please enter a valid DecryptName ')


Substitution_Cipher_Encrypt()
Substitution_Cipher_Decrypt()

