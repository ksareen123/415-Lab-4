#Used and edited by Krish Sareen

# This is udpserver.py file
import socket                       


def polyalpha_enc(plaintxt,key):
    ciphertext = ""
    print("using key " + key)
    textsize = len(plaintxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(plaintxt[i]) + ord(key[i % keysize])
        #print("Adding " + plaintxt[i] + " (" + str(ord(plaintxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        ciphertext += (chr(encryptedchar))

    return ciphertext

    
def polyalpha_dec(ciphertxt,key):
    plaintxt = ""
    print("using key " + key)
    textsize = len(ciphertxt)
    keysize = len(key)
    for i in range (textsize):
        encryptedchar = ord(ciphertxt[i]) - ord(key[i % keysize])
        #print("Subtracting " + str(i) + " index: " + ciphertxt[i] + " (" + str(ord(ciphertxt[i])) + ") " + key[i % keysize] + " (" + str(ord(key[i % keysize])) + ") " + " = " + str(encryptedchar % 128)) 
        encryptedchar = encryptedchar % 128
        plaintxt += (chr(encryptedchar))
    return str(plaintxt)

# create a UDP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Get local machine address
ip = "10.228.23.134"                          

# Set port number for this server
port = 13000                                          

# Bind to the port
serversocket.bind((ip, port))           

print("Waiting to receive message on port " + str(port) + '\n')

polykey = ""
# Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
data, addr = serversocket.recvfrom(1024)
print("received polyalphabetic cipherkey: " + data.decode())
polykey = data.decode()

#send acknowledgement
ack = "Connection established. Key: " + str(polykey)
print("sent acknowledgement")
sent = serversocket.sendto(ack.encode(), addr)

while True:  

   # Receive the data of 1024 bytes maximum. Need to use recvfrom because there is not connecction
   data, addr = serversocket.recvfrom(1024)
   print("received encrypted: " + data.decode())

   msg = data.decode()
   print("decrypted: " + polyalpha_dec(msg, polykey))

   print("Type your reply below")
   reply = input("->")  

   encryptedreply = polyalpha_enc(reply, polykey)
   
   if (reply == "bye"):
      print("")
      print("Waiting to receive message on port " + str(port) + '\n')
      sent = serversocket.sendto(reply.encode(), addr)

   else:
      print('sent ' + encryptedreply)
      sent = serversocket.sendto(encryptedreply.encode(), addr)

   

