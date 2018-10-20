def pressed():
    global press
    numL, numK, numA = map(int, input().split())
    frequency = list(map(int, input().strip().split()))
    frequency = sorted(frequency, reverse = True)
    count = 0
    freqCount = 0
    for i in range(0, numA, numK):
        count += 1
        upperJ = i+numK
        if upperJ > numA:
            upperJ = numA
        for j in range(i, upperJ):
            freqCount += frequency[j] 
        press += (count * freqCount) 
        freqCount = 0


numTimes = int(input())
press = 0
for num in range(numTimes):
    press = 0
    pressed()
    print("Case #",num+1,":", sep='', end='')
    print("",press)
