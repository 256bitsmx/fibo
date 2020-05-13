def fibo(n):
    '''
    fibo
    '''
    assert n >= 0, 'n is lower or equal to zero'
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-2) + fibo(n-1)



from collections import defaultdict

memo = defaultdict(int)
memo[0] = 0
memo[1] = 1

def fibo_dynamic(n):
    '''
    fibo memoization
    '''
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibo_dynamic(n-2) + fibo_dynamic(n-1)
        return memo[n]


assert fibo(0) == 0, 'wrong!'
print(fibo_dynamic(100))

'''
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
'''