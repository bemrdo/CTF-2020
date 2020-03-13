import sys
from base64 import *
from numpy.linalg import inv
# -*- coding: utf-8 -*-

def textToMatrix(text):
    text = b64decode(text).decode('utf-8')
    text = text.strip()
    text = list(text)
    matrix = []
    while True:
        if len(text)%2 != 0:
            text.append(" ")
        else:
            break
    counter= 0
    for i in range(len(text)//2):
        temp = []
        for j in range(counter,counter+2):
            temp.append(ord(text[counter]))
            counter += 1
        matrix.append(temp)
    return matrix

def matrixToText(matrix):
    cipher = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = chr(matrix[i][j])
        cipher += ''.join(matrix[i])
    return cipher

def decrypt(plaintext,key):
    ciphertext = []
    for x in range(len(plaintext)):
        row = []
        for y in range(len(key[0])):
            total = 0
            for z in range(len(key)):
                total = total + (plaintext[x][z] * key[z][y])
            row.append(total)
        ciphertext.append(row)
    return ciphertext

def invKey(key):
    newkey = []
    counter = 0
    for i in range(2):
        temp = []
        for j in range(2):
            temp.append(ord(key[counter]))
            counter += 1
        newkey.append(temp)
    invkey = inv(newkey)
    return invkey

def matrixToText(matrix):
    plaintext = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = chr(int(round(matrix[i][j])))
        plaintext += ''.join(matrix[i])
    return(plaintext)

def main():
    cipher = open('flag', 'rb').read()
    cipher = textToMatrix(cipher)
    key = "ASDF"
    newkey = invKey(key)
    plaintext = decrypt(cipher, newkey)
    #print (cipher)
    print (matrixToText(plaintext))
    #key = [[4.083, 0.833], [-3.172, 0.704]]

if __name__ == "__main__":
    main()
