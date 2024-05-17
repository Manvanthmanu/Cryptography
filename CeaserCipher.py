import random

lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"
capitalAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = '0123456789'
symbols = '!@#$%^&*?'


# -----------------------------------------------------------------------------------
#  Encryption 
def ceaser_Cipher_Encrypt_Algorithm(letter , shiftNum):
    try:
        # handling spaces
        if(letter==' '):
            ReplaceText = random.choice(symbols)
            return(ReplaceText)
        
        elif(letter in numeric):

            numericIndex = numeric.find(letter)
            numericLength = len(numeric)-1

            if(numericIndex+shiftNum > numericLength):
                errorcontrol = (numericIndex + shiftNum) - numericLength
                ReplaceText = numeric[errorcontrol-1]
                return(ReplaceText)
            else:
                ReplaceText= numeric[numericIndex+shiftNum]
                return(ReplaceText)
        
        # handing capital letters
        elif(letter in capitalAlphabets):

            letterIndex = capitalAlphabets.find(letter)
            capitalLength = len(capitalAlphabets)-1

            if(letterIndex+shiftNum > capitalLength):
                errorcontrol = (letterIndex+shiftNum) - (capitalLength)
                ReplaceText=capitalAlphabets[errorcontrol-1]
                return(ReplaceText)
            else:
                ReplaceText=capitalAlphabets[letterIndex+shiftNum]
                return(ReplaceText)
            
        # handling lower letters
        else:

            letterIndex = lowerAlphabets.find(letter)
            lowerLength = len(lowerAlphabets)-1

            if(letterIndex+shiftNum > lowerLength):
                errorcontrol = (letterIndex+shiftNum) - lowerLength
                ReplaceText=lowerAlphabets[errorcontrol-1]
                return(ReplaceText)
            else:
                ReplaceText = lowerAlphabets[letterIndex+shiftNum]
                return(ReplaceText)
            
    except Exception as e:
        return e


def ceaser_Cipher_Encript(encriptText , shiftNum):
    try:
        encriptedList = [ceaser_Cipher_Encrypt_Algorithm(letter,shiftNum) for letter in encriptText ]
        return(''.join(encriptedList))
    except Exception as e:
        print(e)
        




# ---------------------------------------------------------------
# Decription  
def ceaser_Cipher_Decrypt_Algorithm(letter , shiftNum):
    if(letter in symbols):
        ReplaceText = ' '
        return(ReplaceText)

    elif(letter in numeric):
        numericIndex = numeric.find(letter)
        ReplaceText= numeric[numericIndex-shiftNum]
        return(ReplaceText)
    elif(letter in capitalAlphabets):
        letterIndex = capitalAlphabets.find(letter)
        ReplaceText = capitalAlphabets[letterIndex-shiftNum]
        return(ReplaceText)
        
    else:
        letterIndex = lowerAlphabets.find(letter)
        ReplaceText = lowerAlphabets[letterIndex-shiftNum]
        return(ReplaceText)

def ceaser_Cipher_Decrypt(decriptText , shiftnum):
    try:
        mainlist = [ceaser_Cipher_Decrypt_Algorithm(letter,shiftnum) for letter in decriptText ]
        return(''.join(mainlist))
    except Exception as e:
        print(e)
        


print(ceaser_Cipher_Encript('1234567890' , 2))