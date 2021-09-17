n=int(input())
if all(n%i!=0 for i in range(2,n)):
	print("prime")
else:
	print("not a prime")