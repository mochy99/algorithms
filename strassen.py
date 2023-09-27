
Aa = [[4,5,2,5],
      [7,2,9,8],
      [22,5,8,6],
      [4,5,7,2]]
Ba = [[14,1,2,5],
      [7,12,7,7],
      [3,5,2,6],
      [4,6,3,9]]
def trassen(X, Y):
    n = len(X[0])
    if (n == 1):
        result = [[X[0][0] * Y[0][0]]]
        return result
    
    # Divided into subproblem
    n2 = n // 2
    A = [] 
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    for i in range(n2): 
        A.append(X[i][:n2])
        B.append(X[i][n2:])
        C.append(X[i + n2][:n2])
        D.append(X[i + n2][n2:])
        E.append(Y[i][:n2])
        F.append(Y[i][n2:])
        G.append(Y[i + n2][:n2])
        H.append(Y[i + n2][n2:])
    # print(A)
    # print(B)
    # print(C)
    # print(D)


    # the 7 products
    P1 = trassen(A, sub(F, H))
    P2 = trassen(add(A, B), H)
    P3 = trassen(add(C, D), E)
    P4 = trassen(D, sub(G, E))
    P5 = trassen(add(A, D), add(E, H))
    P6 = trassen(sub(B, D), add(G, H))
    P7 = trassen(sub(A, C), add(E, F))

    # return 4 sub matrix
    first = add(add(P5, P6), sub(P4, P2))
    second = add(P1, P2)
    third = add(P3, P4)
    forth = add(add(P1, P7), sub(P5, P3))
    #combine result
    result = []
    for i in range(n2):
        result.append(first[i] + second[i])
    for i in range(n2):
        result.append(third[i] + forth[i])
    
    return result

def add (A, B):
    result = []
    
    for i in range(len(A)):
        tem = []
        for j in range(len(A[0])):
            tem.append(A[i][j] + B[i][j])
        result.append(tem)
    return result

def sub (A, B):
    result = []
    
    for i in range(len(A)):
        tem = []
        for j in range(len(A[0])):
            tem.append(A[i][j] - B[i][j])
        result.append(tem)
    return result

print(trassen(Aa, Ba))

