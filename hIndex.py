import random
def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    result = 0
    n = len(citations)
    def selection(citations, start, end):
        nonlocal result
        if start >= end:
            return result
        
        border = swap(citations, start, end)
        
        print('border ' + str(border))
        print('quantity books more than ' + str(citations[border -1]) + ' is ' + str(n-border))
        if citations[border - 1] <= n - border: 
            result = min(citations[border - 1], n - border)
            return selection(citations, border, end)
        else:
            return selection(citations, start, border - 1)
    
    def swap(citations, start, end):
        k = random.randint(start, end -1)
        pivot = citations[k]
        citations[start], citations[k] = citations[k], citations[start]
        border = start + 1
        for index in range (start + 1, end):
            if citations[index] < pivot:
                citations[border], citations[index] = citations[index], citations[border]
                border += 1
        citations[start], citations[border - 1] = citations[border - 1], citations[start]
        print(border)
        print(pivot)
        print(citations)
        return border
        
    return selection(citations, 0, len(citations))



