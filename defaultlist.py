def list():
	l1=[1,2,3,4,5,6,7,8,9]	
	a=[]
	print(l1)
	for i in l1:
		if (i%2==0):
			a.append(i)
	return("even no:",a)

print(list())
