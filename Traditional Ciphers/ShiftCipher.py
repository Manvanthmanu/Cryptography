import random

def get_input_text():
    return input('Please type the text to encode: ')

def split_text(text):
    return text.split(' ')

def encrypt_word(word):
    listit = list(word)
    if len(listit) > 3:
        listit.append(listit[0])
        listit.pop(0)
        for _ in range(3):
            listit.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        for _ in range(3):
            listit.insert(0, random.choice('abcdefghijklmnopqrstuvwxyz'))
    else:
        listit = listit[::-1]
    return ''.join(listit)

def decrypt_word(encrypted_word):
    listit = list(encrypted_word)
    if len(listit) > 3:
        for i in range(3):
            listit.pop(0)
        for i in range(3):
            listit.pop(-1)
        listit.insert(0,listit[-1])
        listit.pop()
    else:
        listit.reverse()
    return ''.join(listit)


def encrypt_text(text):
    textstring = split_text(text)
    mainlist = [encrypt_word(word) for word in textstring]
    return ' '.join(mainlist)

def decrypt_text(encrypted_text):
    encrypted_words = split_text(encrypted_text)
    mainlist = [decrypt_word(word) for word in encrypted_words]
    return ' '.join(mainlist)

def main():
    text = get_input_text()
    encrypted_text = encrypt_text(text)
    print(encrypted_text)
    decrypted_text = decrypt_text(encrypted_text)
    print(decrypted_text)

if __name__ == "__main__":
    main()