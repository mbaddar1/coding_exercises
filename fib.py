def solution(A):
    n = len(A)

    fib_set = set()
    fib_i_2 = 0
    fib_i_1 = 1
    fib_i = fib_i_2+fib_i_1
    fib_set.add(fib_i)

    while fib_i <=n:
        fib_set.add(fib_i)
        fib_i = fib_i_2 + fib_i_1
        fib_i_2 = fib_i_1
        fib_i_1 = fib_i

    if n in fib_set:
        return 1

    B = [-1]*(n+1)
    last_fib_idx = -1
    for i in range(n+1):
        if i==n or (A[i]==1 and i < n ):
            if (i+1) in fib_set:
                B[i]= 1
                last_fib_idx = i
            elif last_fib_idx >=0:
                diff = i -last_fib_idx
                if diff in fib_set:
                    B[i] = 1 + B[last_fib_idx]
                    last_fib_idx = i
    k = -1 if B[n]+1==0 else B[n]+1

    return k

A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
A1 = [0,0,1,0]
print(solution(A))