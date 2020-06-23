#
def tenodd():
    nnum = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        nnum[i] = input('Enter integer ' + str(i+1) + ': ')
        
    alls = sorted(nnum, reverse=True)

    for i in range(10):
        isodd = int(alls[i])
        if isodd % 2 != 0:
            show = 'largest odd is ' + str(isodd)
            break
        elif i == 9:
            show = 'There are no odd numbers'
            break
    print(show)

tenodd()
