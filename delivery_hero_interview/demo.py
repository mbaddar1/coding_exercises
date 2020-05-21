def solution(A):
    # write your code in Python 3.6
    N = len(A)
    A = countingSort(A)
    if A[0] > 1:
        return 1

    #A[0] <=1
    for i in range(1,N):
        if not (A[i]-A[i-1] <=1):
            if A[i]>1 and A[i-1] >1:
                return  A[i-1]+1
            if A[i-1] <1 <A[i]:
                return 1
            if A[i-1]==1:
                return A[i-1]+1
            if A[i] ==1:
                continue
    if A[N-1] >0:
        return A[N-1]+1
    else: return 1

def countingSort(a):
    min_ = min(a)
    max_ = max(a)
    cnt = [0] * (max_ - min_ + 1)
    for x in a:
        cnt[x - min_] += 1

    return [x for x, n in enumerate(cnt, start=min_)
            for i in range(n)]


A1= [1, 3, 6, 4, 1, 2]
A2= [1, 2, 3]
A3= [-1, -3]
A4 = [4]
A5 = [-4]
A6 = [1]
A7=[-5,5]
r = solution(A7)
print(r)