def my_len(A,i,j,len_dict):
    if (i,j) not in len_dict.keys():
        l = 0
        for idx in range(i,j+1):
            l += A[idx]
        len_dict[(i,j)]=l
        return l
    else :return len_dict[(i,j)]
def solution(K, A):
    N = len(A)
    if N==1:
        return 1 if A[0]>=K else 0
    len_dict = {}
    tot_len = my_len(A,0,N-1,len_dict)
    if tot_len <K:
        return 0
    maximal_no_ropes = 1
    indices = [(0,N-1)]
    while len(indices)>0:
        i,j = indices.pop()
        for l in range(i,j+1):
            len1 = my_len(A,i,l,len_dict)
            len2 = my_len(A,l+1,j,len_dict)
            if len1 >=K and len2>=K:
                maximal_no_ropes +=1
                indices.append((i,l))
                indices.append((l+1, j))
                break
    return maximal_no_ropes


K=4
A= [1, 2, 3, 4, 1, 1, 3]

A1=list(range(10,100))
K1=5

A2= [4,5,6,10]
K2=1

A3 = [10]
K3=20
r = solution(K1,A1)
print(r)