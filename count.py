even_count,odd_count=0,0
list=[1,2,3,4,5,6,7,8,9,10]
for num in list:
	if num%2==0:
		even_count=even_count+1
	else:
		odd_count=odd_count+1
print("even numbers:",even_count)
print("odd numbers:",odd_count)