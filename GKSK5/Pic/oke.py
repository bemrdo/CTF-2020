c = open('gambar2.png','rb').read()
c = c.replace("\xaa\xaa\xaa\xaa", "1").replace("\xff\xff\xff\xff", "0")
b = ''
flag = ''

for i in c:
    if i in '01':
        b += i

for x in range(0, len(b), 8):
    flag += chr(int(b[x:x+8], 2))

print flag

