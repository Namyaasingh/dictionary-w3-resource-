dic={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
list=[]
for value in dic.values():
    list.append(value)
print(list)
i=0
while i<len(list):
    # j=0
    # while j<len(list):
    print(list[i][4])
        # j=j+1
    i=i+1