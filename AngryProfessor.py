def pressed():
    numL, numK, numA = map(int, input().split())
    frequency = list(map(int, input().strip().split()))
    frequency = sorted(frequency, reverse = True)
    press = 0
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
    print(press)


numTimes = int(input())
for num in range(numTimes):
    pressed()
