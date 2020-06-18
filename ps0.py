import numpy

var1 = int(input("Enter number x: "))
var2 = int(input("Enter number y: "))

sol1 = var1**var2
sol2 = int(numpy.log2(var1))

print('x**y = ' + repr(sol1))
print('log(x) = ' + repr(sol2))
