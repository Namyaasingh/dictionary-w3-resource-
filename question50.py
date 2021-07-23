dictionary = { 
               'C1' : [10,20,30], 
               'C2' : [20,30,40],
               'C3' : [12,34]
             }
for key in dictionary.keys():
    dictionary[key].clear()
print(dictionary)