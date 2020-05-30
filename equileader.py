def solution(A):
    n = len(A)
    if n<=1:
        return 0
    B = [(0,0)]*n
    size = 0
    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
        if size >0:
            B[k]=(value,1)
    C = [(0, 0)] * n
    size = 0
    for k in range(n-1,-1,-1):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
        if size >0:
            C[k]=(value,1)
    count = 0
    for k in range(n-1):
        xB = B[k]
        xC = C[k + 1]
        c1 = B[k][1] ==1
        c2 = (C[k+1][1])==1
        c3 = (B[k][0])==(C[k+1][0])

        if (B[k][1]) ==1 and (C[k+1][1]==1) and (B[k][0])==(C[k+1][0]):
            count+=1
            #vprint(f'split k  = {k}')
    return count

A = [4, 3, 4, 4, 4, 2]
A1 = [4, 4, 2, 5, 3, 4, 4, 4]
print(solution(A1))
