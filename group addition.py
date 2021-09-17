print("enter the number")
x,sum,m=int(input),0,None
print("the sum of",x)
while x>0:
	m=x%10
	m=int(m)
	sum=sum+m
	x=x\10
	x=int(x)
print(sum)