def threeodd():
    var_x = input("Enter a number for x: ")
    var_y = input("Enter a number for y: ")
    var_z = input("Enter a number for z: ")

    allin = [var_x, var_y, var_z]
    alls = sorted(allin, reverse=True)
    y = 0
    x = 3
    while (x != 0):
        isodd = int(alls[y])
        if isodd%2 != 0:
            show = 'largest odd is ' + str(isodd)
            x = 0
        elif x == 1 and y == 2:
            show = 'There are no odd numbers'
            x = 0
        else:
            x -= 1
            y += 1
    print(show)
#    print(alls)
#    print(isodd)

threeodd()
