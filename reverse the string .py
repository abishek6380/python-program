str=input()
rev=" "
j=len(str)-1
for i in range(len(str)):
	rev=rev+str[j]
	j=j-1
print(rev)