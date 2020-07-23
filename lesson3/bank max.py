a = int(input())
l1 = [500, 200, 100, 50, 20, 10]
for i in l1:
	if a // i:
		print(a // i, i)
		a = a - (a // i)*i