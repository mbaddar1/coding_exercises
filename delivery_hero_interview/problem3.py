# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sorted_A = sorted(A)
    N = len(A)
    if N < 3:
        return 0
    for Q in range(1, N - 1):
        P = Q - 1
        R = Q + 1
        valid_lengths = (sorted_A[P] > 0) and (sorted_A[Q] > 0) and (sorted_A[R] > 0)
        if valid_lengths and (sorted_A[P] + sorted_A[Q] > sorted_A[R]):
            return 1
    return 0

#A = [10, 2, 5, 1, 8, 20]
#A = [10, 50, 5, 1]
#A = [5,5,10]
A = [-5,5,5,10]
r = solution(A)
print(r)


