# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
# a=[]
# for i in color_dict.keys():
#     a.append(i)
# print(a)
# j=0
# while j<len(a)-1:
#     # k=0
#     # while k<len(a[j])-1:
#         f=(a[j][0])
#         g=(a[j+1][0])
#         if f>g:
#             a[j],a[j+1]=a[j+1],a[j]
#         j=j+1
# print(a)


color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
a=[]
for i in color_dict.keys():
    a.append(i)
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i][0]<a[j][0]:
            a[i],a[j]=a[j],a[i]
        elif a[i][0]==a[i][0]:
            s=0
            while s<len(a[i]):
                if a[i]<a[j]:
                    a[i],a[j]=a[j],a[i]
                s=s+1
        j=j+1
    i=i+1
print(a) 
                
                



# list1=["rubina","apple","red","green","black","white"]
# i=0
# j=1
# while i<len(list1):

#     if list1[i]<list1[j]:
#         a=list1[i]
#         list1[i]=list1[j]
#         list1[j]=a
#         j=j+1
#     i=i+1
# # print(list1)