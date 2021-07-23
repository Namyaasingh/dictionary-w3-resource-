list=[{"item":"item1","amount":400},{"item":"item2","amount":300},{"item":"item1","amount":750}]
dict={}
sum=0
sum1=0
for i in list:
    if "item1" in i["item"]:
        sum=sum+i["amount"]
        dict["item"]=sum
    else:
        sum1=sum1+i["amount"]
        dict["item2"]=sum
print(dict)