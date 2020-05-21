"""

https://www.programcreek.com/2014/04/leetcode-longest-increasing-subsequence-java/
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example, given [10, 9, 2, 5, 3, 7, 101, 18], the longest increasing subsequence is [2, 3, 7, 101]. Therefore the length is 4.


"""

import numpy as np
a = [10, 9, 2, 5, 3, 7, 101, 18]

dp_arr = np.empty(shape=(len(a),len(a)),dtype=object)

for j in range(len(a)):
    dp_arr[j,j] = (j,1)

print(dp_arr)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        idx = dp_arr[i,j-1][0]
        if a[j]> a[idx]:
            new_index = j
            new_len = dp_arr[i,j-1][1]+ 1
            dp_arr[i,j] = (new_index,new_len)
        else:
            new_index = idx
            new_len = dp_arr[i, j-1][1]
            dp_arr[i,j] = (idx,new_len)
        print(dp_arr)
print(dp_arr)