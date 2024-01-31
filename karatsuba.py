#input: two n-digit number x and y
#output: the product of x and y
#using karatsuba multiplication
def karatsuba(x, y):
    n = len(str(x))
    
    if n == 1:
        return x * y
    
    n2 = n // 2
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    result = ac * 10**(2 * n2) + ad_bc * 10**n2 + bd
    
    return result


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
#print(3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627)
