def solution(A, B, C):
        # write your code in Python 3.6
        AB = list(zip(A, B))
        AB_sorted = sorted(AB, key=lambda tup: tup[0])
        N = len(A)
        M = len(C)
        nailed_planks = 0
        nails = 0
        m = 0
        while m < M and nailed_planks < N:

            lower = 0
            upper = N - 1
            while (lower <= upper) and (nailed_planks < N) :
                mid = (lower + upper) // 2
                if AB[mid][0] <= C[m] <= AB[mid][1]:
                    nailed_planks += 1
                    nails +=1
                if C[m] <= AB[mid][0]:
                    upper = mid - 1
                else:
                    lower = mid + 1
            m +=1

        if nailed_planks == N:
            return nails
        else:
            return -1
A = [2]
B = [2]
C = [2]

s = solution(A, B, C)
print(f'solution = {s}')
