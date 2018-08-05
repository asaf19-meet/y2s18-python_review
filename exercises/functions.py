# Write your solution for 1.4 here!

def is_prime(x):
	for i in range(2,x):
		if x%i==0:
			return False
			pass
		else:
			return True

check1=is_prime(31)
check2=is_prime(32)
check3=is_prime(48)
print(check1)
print(check2)
print(check3)