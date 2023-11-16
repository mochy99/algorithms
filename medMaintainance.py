from convertArray import convertArray #input file.text #output array
from heap import low_heapify, high_heapify, extractMax, extractMin #input array already added new element #output heap with proper invariant
from test import test

prev = None
hLow, hHigh = [], []
def computeMed(array, k):
    array.append(k)
    global prev
    if not prev:
        hLow.append(k)
        high_heapify(hLow)
    else:
        if prev > k:
            hLow.append(k)
            high_heapify(hLow)
        else:
            hHigh.append(k)
            low_heapify(hHigh)
    
    if len(hLow) - len(hHigh) > 1:
        newVal = extractMax(hLow)
        hHigh.append(newVal)
        low_heapify(hHigh)
    elif len(hHigh) - len(hLow) > 1:
        newVal = extractMin(hHigh)
        hLow.append(newVal)
        high_heapify(hLow)
    med = None
    if len(array) % 2 == 0:
        med = hLow[0]
    else:
        if len(hHigh) > len(hLow):
            med = hHigh[0]
        else:
            med = hLow[0]

    prev = med
    return med
def medMaintain(input):
    array = []
    sum = 0
    for num in input:
        med = computeMed(array, num)
        sum += med
    result = sum % 10000
    return int(result)

testCase1 = convertArray("testCase/textMedianMaintainance.txt")
case1 = medMaintain(testCase1)
print(test(1, case1, 9335))


