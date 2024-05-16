import random

lowerAlphabets = "abcdefghijklmnopqrstuvwxyz"
capitalAlphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = '0123456789'
symbols = '!@#$%^&*?'


# -----------------------------------------------------------------------------------
#  Encryption 
def ceaser_Cipher_Encrypt_Algorithm(letters , rotatenum):
    try:
        if(letters==' '):
            newcode = random.choice(symbols)
            return(newcode)
        elif(letters in numeric):
            numericIndex = numeric.find(letters)
            if(numericIndex+rotatenum >len(numeric)-1):
                errorcontrol = (numericIndex + rotatenum) - (len(numeric)-1)
                newcode = numeric[errorcontrol-1]
                return(newcode)
            else:
                newcode= numeric[numericIndex+rotatenum]
                return(newcode)
        elif(letters in capitalAlphabets):
            letterIndex =capitalAlphabets.find(letters)
            if(letterIndex+rotatenum > len(capitalAlphabets)-1):
                errorcontrol = (letterIndex+rotatenum) - (len(capitalAlphabets)-1)
                newcode=capitalAlphabets[errorcontrol-1]
                return(newcode)
            else:
                newcode=capitalAlphabets[letterIndex+rotatenum]
                return(newcode)
        else:
            letterIndex = lowerAlphabets.find(letters)
            if(letterIndex+rotatenum > len(lowerAlphabets)-1):
                errorcontrol = (letterIndex+rotatenum) - (len(lowerAlphabets)-1)
                newcode=lowerAlphabets[errorcontrol-1]
                return(newcode)

            else:
                newcode = lowerAlphabets[letterIndex+rotatenum]
                return(newcode)
    except Exception as e:
        return e


def ceaser_Cipher_Encript(encriptText , shiftnum):
    try:
        mainlist = [ceaser_Cipher_Encrypt_Algorithm(encriptletters,shiftnum) for encriptletters in encriptText ]
        return(''.join(mainlist))
    except:
        print(ceaser_Cipher_Encrypt_Algorithm)




# ---------------------------------------------------------------
# Decription  
def ceaser_Cipher_Decrypt_Algorithm(letters , rotatenum):
    if(letters in symbols):
        newcode = ' '
        return(newcode)

    elif(letters in numeric):
        numericIndex = numeric.find(letters)
        newcode= numeric[numericIndex-rotatenum]
        return(newcode)
    elif(letters in capitalAlphabets):
        letterIndex = capitalAlphabets.find(letters)
        newcode = capitalAlphabets[letterIndex-rotatenum]
        return(newcode)
        
    else:
        letterIndex = lowerAlphabets.find(letters)
        newcode = lowerAlphabets[letterIndex-rotatenum]
        return(newcode)

def ceaser_Cipher_Decrypt(decriptText , shiftnum):
    try:
        mainlist = [ceaser_Cipher_Decrypt_Algorithm(decriptletters,shiftnum) for decriptletters in decriptText ]
        return(''.join(mainlist))
    except:
        print(ceaser_Cipher_Decrypt_Algorithm)


