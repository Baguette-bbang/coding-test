month = int(input())
allMonth =[12,1,2,3,4,5,6,7,8,9,10,11]
if month in allMonth[0:3]:
    print('winter')
elif month in allMonth[3:6]:
    print('spring')
elif month in allMonth[6:9]:
    print('summer')
else : print('fall')