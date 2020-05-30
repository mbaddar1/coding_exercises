"""
link
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

Task description
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

link

"""
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    swap_counter = 0
    idx = 0
    while (swap_counter <n) and (idx <n):
        if A[idx] == idx+1:
            idx +=1
            continue
        elif not (0<=A[idx]<=n):
            return 0

        if A[A[idx]-1]==A[idx]:
            return 0
        tmp = A[idx]
        A[idx] = A[tmp-1]
        A[tmp-1] = tmp
        swap_counter+=1

    return 1 if idx==n else 0

A = [4, 1, 3, 2]
A1 = [4, 3, 2]
A2 = [3,1,2,3,3]
A3  = list (range(1000,0,-1))

A4 = [1]
r = solution(A3)
print(r)