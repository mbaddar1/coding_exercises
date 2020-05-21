# def min_ij(A,i,j):
#     min_ = 1000000000+1
#     for l in range(i,j+1):
#         min_ = min(min_,A[l])
#     return min_
def solution(H):
    # write your code in Python 3.6
    N = len(H)

    max_height = max(H)
    bricks = 0
    while max_height > 0:

        i = -1
        j=0
        running_min_height = 10000000000000+1
        while j<N:

            if H[j]>0:
                if i==-1: i=j
                running_min_height = min(H[j],running_min_height)
            x1= H[j]==0
            x2 = j==N-1
            if (H[j]==0) or (j==N-1):

                if i>=0:
                    bricks +=1
                    idx = None
                    if H[j]==0:
                        idx = range(i,j)
                    else: idx = range(i,j+1)
                    old_max_height = max_height
                    for l in idx:

                        H[l] -=running_min_height
                i=-1
                running_min_height = 10000000000000 + 1

            j+=1
        max_height = max(H)
    return bricks




H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(H))