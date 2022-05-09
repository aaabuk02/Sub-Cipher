import sys
import string

cipher = dict()
key = int(sys.argv[1])

for i in range(len(string.ascii_letters)):
    cipher[string.ascii_letters[i]] = string.ascii_letters[(i + key) % 52]

plainText = sys.argv[2]
encryptedText = ""

for plainLine in plainText:
    for char in plainLine:
        encryptedText += (cipher[char])

print(encryptedText)