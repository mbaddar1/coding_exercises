"""
4.1. Exercise
Problem: You are given an integer m (1 � m � 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 � ai, bi � m).
The goal is to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap. By swap operation we mean picking one element from array A and
one element from array B and exchanging them.
"""


def gen_count_arr(A, m):
    n = len(A)
    A_count = [0] * (m + 1)
    for i in range(n):
        A_count[A[i]] += 1
    return A_count


def solution(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    m = max([max(A), max(B)])

    A_count = gen_count_arr(A, m)
    B_count = gen_count_arr(B, m)
    M = len(A_count)
    i = 0
    j = 0

    while i < M and j < M:
        if A_count[i] == 0:
            i += 1
            continue
        if B_count[j] == 0:
            j += 1
            continue
        new_sum_A = sum_A + j - i
        new_sum_B = sum_B + i - j
        if new_sum_A == new_sum_B:
            return 1
        if new_sum_A > new_sum_B:
            i += 1
        else:
            j += 1
    return 0


A = [1, 1, 4]
B = [2, 1, 5]
print(solution(A, B))
