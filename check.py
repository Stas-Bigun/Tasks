def check(arg1):
	if 0 == arg1:
		return "You choose zero"
	elif 0 < arg1:
		return "+"
	else:
		return "-"
	
a = int(input("Enter number\n"))
print (check(a))