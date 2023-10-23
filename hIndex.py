
def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort()
    result = 0
    n = len(citations)
    for i in range(n - 1, -1, -1):
        if citations[i] >= n - i:
            result = min(citations[i], n - i)
    return result



input_list = [1,0,3,5,6]
index = hIndex(input_list)
print(index) 
