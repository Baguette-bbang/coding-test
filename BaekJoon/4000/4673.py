limit = 10000
nonSelfList= [i for i in range(1,limit+1)]
selfList = []
def sum_digit(number):
    return number + sum([int(i) for i in str(number)])

def nonSelf():
    for i in range(1, limit+1):
        selfNum = sum_digit(i)
        if selfNum <= limit and selfNum in nonSelfList:
            nonSelfList.remove(selfNum)
nonSelf() 
for num in sorted(nonSelfList):
    print(num)