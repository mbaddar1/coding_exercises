"""

https://codility.com/media/train/7-MaxSlice.pdf

Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a0, a1, . . . , an−1 and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total ap + ap+1 + . . . + aq is maximal. We assume
that the slice can be empty and its sum equals 0.
a0 a1 a2 a3 a4 a5 a6
5 -7 3 5 -2 4 -1
In the picture, the slice with the largest sum is highlighted in gray. The sum of this slice
equals 10 and there is no slice with a larger sum. Notice that the slice we are looking for may
contain negative integers, as shown above.

"""
def sum(A,i,j):
    sum = 0
    for l in range(i,j):
        sum+=A[l]
    return sum

def soln_n3(A):
    N = len(A)
    max_sum = 0
    sum_dict = dict()
    for p in range(0,N):
        for q in range(p,N):
            #sum_ = sum(A,p,q)
            if p==0:
                sum_ = sum(A,p,q)
            else:
                sum_ = sum_dict[(p-1,q)]-A[p-1]
                del sum_dict[(p-1,q)]

            sum_dict[(p,q)]=sum_
            max_sum = max(sum_,max_sum)
    return max_sum

def soln_n(A):
    N = len(A)
    B = [0]*(N)
    max_sum = 0
    running_sum  = 0
    # pass1
    max_idx = 0
    for i in range(0,N):
        running_sum+=A[i]
        max_idx = i if running_sum>=max_sum else max_idx
        max_sum = max(max_sum,running_sum)
        B[i] = max_sum

    subtract_sum = 0
    running_subtract = max_sum
    running_max = max_sum
    for j in range(0,max_idx+1):
        running_max = max(running_max, running_subtract)
        running_subtract -=A[j]
    # for j in range(0,N):
    #     B[j+1] = B[j+1]-subtract_sum
    #     max_B = max(max_B,B[j+1])
    #     subtract_sum +=A[j]


    return running_max

A  = [5,-7,3,5,-2,4,-1]
A1 = [-5,5]
r  = soln_n(A1)
print(r)