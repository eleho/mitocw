varX = int(input("Enter an integer: "))
max_pwr = 5
root = 0
pwr = 0
n = 0

if varX >= 0:
    while root**pwr < abs(varX):
        root += 1
        while pwr < max_pwr and root**pwr < abs(varX):
            pwr +=1
#            print("inner while loop " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))
        if root**pwr != abs(varX):
            pwr = 0
#            print("inner if 11 " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))
#        else:
#            print("inner if 12 " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))

else:
    while root**pwr > varX:
        root -= 1
        while pwr < max_pwr and root**pwr > varX:
            pwr +=1
#            print("- inner while loop " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))
        if root**pwr != varX:
            pwr = 0
#            print("- inner if 11 " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))
#        else:
#            print("- inner if 12 " + str(root) + " and " + str(pwr) + " = " + str(root**pwr))

if root**pwr != varX:
    print("No Root and Power pair exist such that Root**Power = " + str(varX))
else:
    print("Root " + str(root) + " to the power " + str(pwr) + " is = " + str(varX))
