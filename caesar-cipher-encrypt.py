#!/usr/bin/python

import argparse

#function to encyrpt
def encrypt(text,s):
    ciphertext = ""
 
    # traverse text
    for i in range(len(text)):
        #char = text[i]
 
        # Encrypt uppercase characters
        if (text[i].isupper()):
            ciphertext = ciphertext+chr((ord(text[i]) + s - 65) % 26 + 65)
            #print (ciphertext)
        # Encrypt lowercase characters
        elif (text[i].islower()):
            ciphertext = ciphertext+chr((ord(text[i]) + s - 97) % 26 + 97)
            #print(ciphertext)
        else:
            ciphertext = ciphertext+" "
            #print (ciphertext)
    return ciphertext
    
#function to decrypt
def decrypt(text,s):
    ciphertext = ""
 
    # traverse text
    for i in range(len(text)):
        #char = text[i]
 
        # Encrypt uppercase characters
        if (text[i].isupper()):
            ciphertext = ciphertext+chr((ord(text[i]) - s - 65) % 26 + 65)
            #print (ciphertext)
        # Encrypt lowercase characters
        elif (text[i].islower()):
            ciphertext = ciphertext+chr((ord(text[i]) - s - 97) % 26 + 97)
            #print(ciphertext)
        else:
            ciphertext = ciphertext+" "
            #print (ciphertext)
    return ciphertext
    
#parsing arguments from cli    
parser = argparse.ArgumentParser()
parser.add_argument('--shift', type=int, required=True)
args = parser.parse_args()
s = args.shift

#reading plain text file
f = open('plain.txt','r',encoding = 'utf-8')
text = f.read()

#opening encrypt text file
encryptedfile = open("encrypt.txt", "w")

#putting contents encyrpted by caesar cipher
encryptedfile.write(encrypt(text,s))
encryptedfile.close()
print ("Caesar Encryption Completed! File Saved: encrypt.txt \n \n")

#reading enrypt text file
encryptedfile = open("encrypt.txt", "r")
print (encryptedfile.read())
encryptedfile.close()