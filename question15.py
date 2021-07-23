my_dict = {'x':500, 'y':5874, 'z': 560}
list=[]
for i in my_dict.values():
    list.append(i)
print(list)
index=0
max=list[0]
while index<len(list):
    if list[index]>max:
        max=list[index]
    index=index+1
print(max)