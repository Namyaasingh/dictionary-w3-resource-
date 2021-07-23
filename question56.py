dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
value=[]
key=[]
for x,y in dic.items():
    value.append(y)
    key.append(x)
    new_list=[]
i=0
while i<len(key):
    g=[key[i],value[i]]
    new_list.append(g)
print(new_list)
# print(key)
# print(value)
# new_list=[]
# i=0
# while i<len(key):
#     g=[key[i],value[i]]
#     new_list.append(g)
# print(new_list)