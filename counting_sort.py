def countingSort(a):
    min_ = min(a)
    max_ = max(a)
    cnt = [0] * (max_ - min_ + 1)
    for x in a:
        cnt[x - min_] += 1

    return [x for x, n in enumerate(cnt, start=min_)
            for i in range(n)]

a = [9,9,9,8,9,6,1,2]
print(countingSort(a))
