n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
print("enter two numbers:")
while(n1!=n2):
	if(n1>n2):
		n1=n1-n2
	else:
		n2=n2-n1
print("gcd",n1)