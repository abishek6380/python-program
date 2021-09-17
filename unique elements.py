arr1=[100,75,20,5,25]
arr2=[20,57,7,100,45]
arr3=arr1+arr2
for item in arr3:
      if item  not in res_arr3:
         res_arr3.append(item)
      print ( "unique element")
      for item in res_arr3:
      	print (item )