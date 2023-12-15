A = "AGTACG"
B = 'ACATAG'
mismatch = 2
gap = 1

prev = [i * gap for i in range(len(B) + 1)]
print(prev)

for i in range(1, len(A) + 1):
    cur = [i * gap]
    for j in range(1, len(B) + 1):
        case1 = prev[j - 1] + mismatch if A[i - 1] != B[j - 1] else prev[j - 1]
        case2 = prev[j] + gap
        case3 = cur[j - 1] + gap
        optimal = min(case1, case2, case3)
        cur.append(optimal)
    prev = cur[:]
    print(prev)
