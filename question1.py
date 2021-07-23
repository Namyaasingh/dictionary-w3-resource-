a={1:2,3:4,4:3,2:1,0:0}
l=list(a.items())
l.sort()
print(l)
l=list(a.items())
l.sort(reverse=True)
print(l)
dict=dict(l)
print(dict)



