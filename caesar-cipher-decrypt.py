#!/usr/bin/python

import argparse
    
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

#reading encrypt text file
f = open('encrypt.txt','r',encoding = 'utf-8')
text = f.read()

#opening plain text file
encryptedfile = open("decrypt.txt", "w")

#putting contents encyrpted by caesar cipher
encryptedfile.write(decrypt(text,s))
encryptedfile.close()
print ("Caesar Decryption Completed! File Saved: decrypt.txt \n \n")

#reading enrypt text file
encryptedfile = open("decrypt.txt", "r")
print (encryptedfile.read())
encryptedfile.close()