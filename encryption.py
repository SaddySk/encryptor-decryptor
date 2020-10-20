# -*- coding: utf-8 -*-
"""
Created on Wednesday 30 October 2019 18:22:50

@author: Sk_Saddy
"""
import os

def Encrypt(password, key):
    # convert key
    convKey = 0
    encrypted = ''
    convPassword = ''
    for k in key:
        convKey += ord(k)
    convKey = convKey*786       #   multiply with 786
    keyValue = convKey%127     #   mod 127
    # encrypt
    for elements in password:
        datafile = ord(elements)*keyValue
        datafile = datafile%127
        datafile = datafile + 32
        encrypted = chr(datafile)
        convPassword += encrypted
    return convPassword

# open the password file
file = open("datafile.txt", "r")
passwd = file.read()

# enter the key to for encryption
key = input()

encryptedPassword =  Encrypt(passwd, key)

newFile = open("datafile.txt", "w+")
newFile.write(encryptedPassword)
