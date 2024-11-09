a = 10
b = 20
a = a * b
b = b + a
print(a)
print(b)
for i in range(2):
	if a:
		a = a * b
	else:
		b = b + a
print(a)
print(b)