listA = [0,1,2,3,4,5,6,7,8,9]
listB = [0,1,2,3,4,5,6,7,8,9]
jx = 5
jy = 6


pad = 0
while pad != len(listA):
    coordsX = listA[pad]
    coordsY = listB[pad]
    if jy+1 == coordsY and jx+1 == coordsX:
        print("c bon")
    pad += 1
    print(coordsX, coordsY)


