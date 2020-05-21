""""
For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].
"""


def solution(A):
    # write your code in Python 3.6
    Kij_1 = abs(A[0])
    abs_Kij_min = Kij_1
    N = len(A)
    for j in range(1, N):
        abs_Kij_min = min([abs(Kij_1 + A[j]), abs(Kij_1 - A[j])])
        S = 1 if abs(Kij_1 + A[j]) < abs(Kij_1 - A[j]) else -1
        Kij_1 += A[j] * S
    return abs_Kij_min


A = [3, 3, 3, 4, 5]
print(solution(A))
