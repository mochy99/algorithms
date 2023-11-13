from convertArray import convertArray #input file.text #output array
from heap import low_heapify, high_heapify #input array already added new element #output heap with proper invariant
from extractMin import extractMin


input_data = convertArray("textMedianMaintainance.txt")
prev = None
hLow, hHight = [], []
def medMaintain(array, k):
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
            hHight.append(k)
            low_heapify(hHight)
    
    if len(hLow) - len(hHight) > 1:
        newVal = extractMin(hLow)
        hHight.append(newVal)
        low_heapify(hHight)
    elif len(hHight) - len(hLow) > 1:
        newVal = extractMin(hHight)
        hLow.append(newVal)
        high_heapify(hLow)
    print(hLow)
    print(hHight)
    med = None
    if len(array) % 2 == 0:
        med = (hHight[0] + hLow[0]) / 2
    else:
        if len(hHight) > len(hLow):
            med = hHight[0]
        else:
            med = hLow[0]

    prev = med

print(medMaintain([], 1))
print(medMaintain([1], 0))
print(medMaintain([1,0], -2))
print(medMaintain([1,0, -2], 5))
print(medMaintain([1,0, -2,5], 8))
print(medMaintain([1,0, -2,5,8], 11))


