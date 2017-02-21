def Abs(num):
	if num>0:
		return Abs(num-1)+1
	if num <0:
		return Abs(num+1)+1
	if num==0:
		return 0

print "ingrese un numero"
print Abs(int(input()))

	