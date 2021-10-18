a = 1234
l = 3
while l>0:
	b = int(input("Enter the password: "))
	if b==a:
		print("Login Succesfull")
		break
	else:
		print("Password is incorrect")
		print("Attempts Left: ",l-1)
		l -= 1
		if l==0:
			print("Locked out")
