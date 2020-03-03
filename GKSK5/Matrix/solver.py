from base64 import *

def textToMatrix(text):
    cipher = b64decode(text)
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

def decrypt(cipher, key):
    for x in range(len(cipher)):
        row = []
        for y in range(len(key[0])):
            for z in range(len(key)):
                total1 = 1 

def main():
    cipher = open('flag', 'rb').read()
    cipher = textToMatrix(cipher)
    key = 'GKSK'
    print cipher[0]

if __name__ == "__main__":
    main()

