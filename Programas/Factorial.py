def fact(num):
	if num > 0:
		return num * fact(num-1)
	if num < 0:
		return "No exixte el numero factorial"
	if num == 0:
		return 1

print "Ingrese un numero"
print fact(int(input()))