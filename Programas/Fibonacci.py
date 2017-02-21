def fibo(num):
	if num > 2:
		return fibo(num-2) + fibo(num-1)
	if num == 2:
		return 1
	if num == 1:
		return 1
	if num == 0:
		return 0

print "Ingrese un numero"
print fibo(int(input()))