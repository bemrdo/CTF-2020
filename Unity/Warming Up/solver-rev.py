d = '''
85
79
75
87
93
55
54
53
56
114
88
56
63
62
120
106
117
116
96
96
103
112
115
114
93
92
41
40
88
89
90
98'''.split()

flag = ''
for i in range(len(d)):
    flag += chr(i ^ int(d[i]))
print flag
