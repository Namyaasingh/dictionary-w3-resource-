dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 500, 'd':400}
dic4={}
for i,j in dic1.items():
    for x,y in dic2.items():
        if i==x:
            dic4[i]=(j+y)
            print(dic4)
        dic4.update(dic1)
        dic4.update(dic2)

        

