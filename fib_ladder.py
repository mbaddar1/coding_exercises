def get_fib_arr(k):
    if k==0:
        return [0]
    if k==1:
        return [0,1]

    fib_arr = [0]*(k+1)
    fib_arr[0]=0
    fib_arr[1]=1
    for i in range(2,k+1):
        fib_arr[i] = fib_arr[i-1]+fib_arr[i-2]
    return fib_arr

def solution(A,B):
    max_num = max(A)
    fib_arr = get_fib_arr(max_num+1)
    N = len(A)
    C = [0]*N
    for i in range(N):
        fib = fib_arr[A[i]+1]
        two_pow_p = (1 << B[i])
        C[i] = fib & (two_pow_p-1)
    return C

A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
print(solution(A,B))

