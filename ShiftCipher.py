#  Shift Cipher Tradition 
import random

defaultDictionry = {
    'alphabets' : 'abcdefghijklmnopqrstuvwxyz',
    'numbers' : '1234567890',
    'symbols' : '!@#$%^&*()_+=-?><\\/{}[]~`|,.'
}

codeDataBase = {}


def codegen():
    codeList = random.sample(defaultDictionry['alphabets'] ,len(defaultDictionry['alphabets']))
    code = ''.join(codeList)
    return code
print(codegen())
    



# userName = input('please enter the username : ')
# userText = input('Please enter the code to encrypt : ')


# def shift_Cipher_Encript_RandomOrder_Algorithm(letter):
#     letterIndex = defaultDictionry['alphabets'].find(letter)
#     newletter = codegen()[letterIndex]
#     return newletter

# def shift_Cipher_Encript_RandomOrder(userText , userName):
#     codegen = ''.join(codegen())
#     encriptletter = [shift_Cipher_Encript_RandomOrder_Algorithm(letter) for letter in userText]
#     encriptMessage = ''.join(encriptletter)
#     codeDataBase[userName] = codegen


#     return encriptMessage


# print(shift_Cipher_Encript_RandomOrder(userText , userName))
# print(codeDataBase)
