def is_prime(x):
	for i in range(2,x):
		if x%i==0:
			return False
			pass
		else:
			return True

def encode(x, y):
	while is_prime(x)== False:
		x+=1

	while is_prime(y)== False:
		y+=1
		
	if 1<=y<=250 and 500<=x<=1000:
		return x*y
	else:
		print("Invalid input: Outside range")
		return None

def decode(coded_message):
	for x in range(coded_message):
		if coded_message%x==0:
			print(x + ", " + coded_message/x)

print(decode(encode(500,50)))