# -*- coding: utf-8 -*-
"""
Created on Wednesday 30 October 2019 18:22:50

@author: Sk_Saddy
"""
import os

def Decrypt(password, key):
    # convert key
    decrypted = ''
    convPassword = ''
    # encrypt
    for elements in password:
        datafile = ord(elements)-32
        datafile = datafile*key
        datafile = datafile%127
        decrypted = chr(datafile)
        convPassword += decrypted
    return convPassword


# open the password file
file = open("datafile.txt", "r")
password = file.read()

# Enter your key for encryption
key = int(input())

decryptedPassword =  Decrypt(password, key)

newFile = open("datafile.txt", "w+")
newFile.write(decryptedPassword)

file.close()
newFile.close()
print("Passwords Decrypted!")
