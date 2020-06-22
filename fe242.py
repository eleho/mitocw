#
def tenodd():
    count1 = count2 = 10
    pos1 = pos2 = 0
    nnum = [0,0,0,0,0,0,0,0,0,0]
    while count1 != 0:
        nnum[pos1] = input('Enter integer ' + str(pos1+1) + ': ')
        count1 -= 1
        pos1 += 1
    alls = sorted(nnum, reverse=True)
#    print(nnum)
#    print(alls)
#    print(count2)
#    print(pos2)

    while count2 != 0:
        isodd = int(alls[pos2])
        if isodd % 2 != 0:
            show = 'largest odd is ' + str(isodd)
            count2 = 0
        elif count2 == 1 and pos2 == 9:
            show = 'There are no odd numbers'
            count2 = 0
        else:
            count2 -= 1
            pos2 += 1
    print(show)

tenodd()
