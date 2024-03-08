my_list=[]
for values in [10, 20, 30, 40]:
    my_list.append(values)
my_list.insert(1, 15)
for value in [50,60,70]:
    my_list.extend([value])
my_list.pop()
my_list.sort()
index_of_30=my_list.index(30)
print("Enter Index of 30: ", index_of_30)