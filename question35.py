color_dict={'Math':81, 'Physics':83, 'Chemistry':87}
a=[]
key=[]
for l in color_dict.keys():
    key.append(l)
for i in color_dict.values():
    a.append(i)
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        elif a[i]==a[i]:
            a[i],a[j]=a[i],a[j]
        j=j+1
    i=i+1
print(a)
dict={}
index=0
while index<len(a):
    dict[key[index]]=a[index]
    index=index+1
print(dict)


