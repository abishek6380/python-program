arr = [5, 2, 8, 7, 1]
temp =0
print(f"Elements of original array:{arr} ") 
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] > arr[j]):  
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Elements of array sorted in ascending order: ",arr,end=" ")