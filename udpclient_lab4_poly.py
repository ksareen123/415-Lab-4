# This is udpclient.py file

#Import socket programming module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Set destination port
port = 13000

# Include the server Address 
serverAddr = ('10.228.23.134', port)

def polyAlphaEncrypt(plaintext, key):
    cipherASCII = []
    ciphertext = ""
    count = 0
    size = len(key)
    for character in plaintext:
        currentASCII = ord(character)
        newASCII = (currentASCII + ord(key[count])) % 128
        cipherASCII.append(newASCII)
        ciphertext += chr(newASCII)
        count += 1
        count = count % size
    return ciphertext

def polyAlphaDecrypt(ciphertext, key):
    plaintextASCII = []
    plaintext = ""
    count = 0
    size = len(key)
    for character in ciphertext:
        currentASCII = ord(character)
        newASCII = (currentASCII - ord(key[count])) % 128
        plaintextASCII.append(newASCII)
        plaintext += chr(newASCII)
        count += 1
        count = count % size
    return plaintext

#send a key to the server
print("Type your shared key below")
message = input("->")

print("sent: " + message)
s.sendto(message.encode(), serverAddr)

msg, addr = s.recvfrom(1024)
print("received: " + msg.decode())
polyKey = message

while (1):
    # Send message (input from the keyboard). The string needs to be converted to bytes.
    # To send more than one message, please create a loop
  
    
    print("Type your message below")
    message = input("->")

    encryptedmessage = polyAlphaEncrypt(message, polyKey)
    print("sent: " + encryptedmessage)
    s.sendto(encryptedmessage.encode(), serverAddr)
        

    # Receive no more than 1024 bytes
    msg, addr = s.recvfrom(1024)
    print("received: " + msg.decode())

    if (msg.decode() == "bye"):
        # Close connection
        s.close()
        break
    
    decryptedreply = polyAlphaDecrypt(msg.decode(), polyKey)
    print("decrypted: " + decryptedreply)
