dic={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
list={}
count=0
for value in dic.values():
    if count<=1:
        count=count+1
    list.update({value:count})
print(list)



