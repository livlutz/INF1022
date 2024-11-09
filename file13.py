x = 2
y = 3
for i in range(3):
	if x:
		print(x)
		if y:
			print(y)
	else:
		print(0)
	x = x + 1
	y = y * x