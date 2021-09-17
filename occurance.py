my_list = [2,3,4,6,6,5,3,4,8,7] 
print(my_list)
all_indexes = [] 
n=int(input())
for i in range(0, len(my_list)) : 
    if my_list[i] == n : 
        all_indexes.append(i)
print("Indexes for element",n," is:",all_indexes)
print("occurance of",n,"in list is:",my_list.count(n))