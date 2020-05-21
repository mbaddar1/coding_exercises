def solution(A, B):
    # write your code in Python 3.6
    stack = []
    N = len(A)
    fish_counter = N
    for i in range(N):
        if B[i] == 1:
            stack.append(A[i])
        elif B[i] == 0:
            while len(stack)>0:
                fish_size = stack.pop()
                fish_counter -= 1
                if fish_size > A[i]:
                    stack.append(fish_size)
                    break
                # else : the fish in stack is eaten
    return fish_counter


A = [5, 3, 2, 1, 4]
B = [0, 1, 1, 1, 0]

sol = solution(A, B)
print(sol)
