# coding: utf8
c = open('gambar.png','rb').read()
d = c.replace('GKSK', '')
d = d.replace('QWER','')
d = d.replace('SADF','')
d = d.replace('ªªªª', '')
print (d.split("iVBORw0KGgoAAA"))[0]

