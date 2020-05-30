# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def overlap(A, B, i, j):
    return (A[i] <= A[j] <= B[i]) or (A[j] <= A[i] <= B[j])

def solution(A, B):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 1
    counter = 1
    last_seg = 0
    for i in range(1, n):
        if overlap(A, B, last_seg, i):
            pass
        else:
            last_seg = i
            counter +=1
    return counter


A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]

A1= [1,2,4,6]
B1 = [10,11,12,13]
print(solution(A,B))