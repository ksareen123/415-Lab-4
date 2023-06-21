import string

def polyalpha_enc(plaintxt,key):
    ciphertext = ""
    textsize = len(plaintxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(plaintxt[i]) + ord(key[i % keysize])
        print("Adding " + plaintxt[i] + " (" + str(ord(plaintxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        ciphertext += (chr(encryptedchar))

    return ciphertext

    
def polyalpha_dec(ciphertxt,key):
    plaintxt = ""
    textsize = len(ciphertxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(ciphertxt[i]) - ord(key[i % keysize])
        print("Subtracting " + str(i) + " index: " + ciphertxt[i] + " (" + str(ord(ciphertxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        plaintxt += (chr(encryptedchar))
    return str(plaintxt)


message = input("Enter Message->")

key = input("Enter key->")

encrypted = polyalpha_enc(message, key)

print("Encrypted Message: " + encrypted)

decrypted = polyalpha_dec(encrypted, key)

print("Decrypted Message: " + decrypted)


