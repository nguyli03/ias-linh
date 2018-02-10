'''Caesar cipher'''
#!/usr/bin/env python3
#encoding: UTF-8

DICT_ENG = set()

def shift_by_n(word: str, shift: int, direction: int) -> str:
    '''Shifting all letters in a word by n. Direction specifies encryption (>0) or decryption (<0)'''
    # raise NotImplementedError
    res = ''
    punctuation = ";:,.!?'() \n\t"
    for ch in word:
        if ch not in punctuation:
            asc = ord(ch.lower())
            if direction > 0:
                change = asc + shift
                if change > 122:
                    change = 96 + (97 - change)
            else:
                change = asc - shift
                if change < 97:
                    change = 123 - (97 - change)
            res += chr(change)
        else:
            res += ch
    if direction <0:
        res = res.upper()
    return res

def encrypt(plaintext: str, shift: int, obfuscate=False) -> str:
    '''Encrypt and optionally obfuscate a string'''
    cipher = shift_by_n(plaintext, shift, 1).upper()  # 1 for encryption
    if obfuscate:
        punctuation = ";:,.!?'() \n\t"
        for symbol in punctuation:
            cipher = cipher.replace(symbol, '')
    return cipher

def encrypt_file(file_in_name: str, file_out_name: str, shift: int, obfuscate=False):
    '''Encrypt a file and write the cipher to a file'''
    with open(file_in_name, 'r', encoding="utf-8") as file_in:
        plaintext = file_in.read().lower()
    cipher = encrypt(plaintext, shift, obfuscate)
    with open(file_out_name, 'w', encoding="utf-8") as file_out:
        file_out.write(cipher)

def decrypt(cipher: str, shift: int) -> str:
    '''Decrypt a string'''
    # raise NotImplementedError
    cipher = shift_by_n(cipher, shift, -1).lower()  # lower for decrypt
    punctuation = ";:,.!?'()\n\t"
    for symbol in punctuation:
        cipher = cipher.replace(symbol, '')
    return cipher

def decrypt_file(file_in_name: str, file_out_name: str, shift: int):
    '''Decrypt a file that has not been obfuscated'''
    with open(file_in_name, 'r', encoding="utf-8") as file_in:
        cipher = file_in.read()
    plaintext = decrypt(cipher, shift)
    with open(file_out_name, 'w', encoding="utf-8") as file_out:
        file_out.write(plaintext)

def analyze_file(file_in_name: str, file_out_name: str, dictionary: set):
    '''Analyze a file that has been obfuscated'''
    # raise NotImplementedError
    wordlist = open('caesar/wordlist_english.txt')
    for word in wordlist:
        dictionary.add(word.strip().lower())
    f = open(file_in_name,'r')
    fenglish = False
    shift = 0
    for line in f:
        if len(line) <20:
            for word in line.split():
                while not fenglish and shift <26:
                    newword = shift_by_n(word, shift, -1).lower()
                    if newword in dictionary:
                        fenglish = True
                    else:
                        shift += 1
        else:
            numlen = 3
            while not fenglish and shift <26:
                numlen = 3
                shift += 1
                while numlen < 11 and not fenglish:
                    newword = shift_by_n(line[:numlen], shift, -1).lower()
                    if newword in dictionary:
                        # print("new word when it's true: ",newword)
                        # print(shift)
                        fenglish = True
                    else:
                        numlen += 1
    decrypt_file(file_in_name, file_out_name, shift)

def main():
    '''Main function'''
    print('---Caesar cipher---')
    analyze_file('caesar/cipher_1.txt', 'caesar/plaintext_1.txt', DICT_ENG)
    analyze_file('caesar/cipher_2.txt', 'caesar/plaintext_2.txt', DICT_ENG)
    print('---Over and out---')

if __name__ == '__main__':
    main()
