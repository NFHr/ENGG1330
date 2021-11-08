key = int(input('Key: '))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

mode = input('Mode: ')
inputText = input('Message: ')
outputText = ''

if mode == 'E':
    encryptedAlphabet = alphabet[key:] + alphabet[:key]
    for i in inputText:
        if 97 <= ord(i) <= 122:
            outputText += encryptedAlphabet[ord(i)-97]
        else:
            outputText += i

elif mode == 'D':
    decryptedAlphabet = alphabet[-key:] + alphabet[:-key]
    for i in inputText:
        if 97 <= ord(i) <= 122:
            outputText += decryptedAlphabet[ord(i)-97]
        else:
            outputText += i

print(outputText)