def rich_and_quite(l, n):
    a, b, c = 0, 0, 0
    lists = []
    if n == 1:
        return l
    for i in range(10):
        lists.append([])
        for j in range(10):
            lists[i].append('0')
    for q in range(len(l)):
        if a < n and c == 0:
            lists[a][b] = l[q]
            a += 1
        if a >= 0 and c == 1:
            lists[a][b] = l[q]
            a -= 1
            b += 1
        if a == n and c == 0:
            c = 1
            a -= 2
            b += 1
        if a == 0 and c == 1:
            c = 0
    return lists
