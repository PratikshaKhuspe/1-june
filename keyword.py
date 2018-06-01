def printlist(upper_limit,step=1):
	print("upper limit: ",upper_limit)         #keyword argument
	num_list=list(range(0,upper_limit,step))
	print("list is",num_list)

printlist(upper_limit=5,step=2)
