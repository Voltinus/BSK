def railfence_encode(M, n = 3):
    arrs = [[] for i in range(n)]
    
    current = 0
    dir = 1

    for i in M:
        arrs[current].append(i)
        current += dir
        if dir == 1 and current == n-1:
            dir = -1
        if dir == -1 and current == 0:
            dir = 1

    return "".join(["".join(i) for i in arrs])


def railfence_decode(M, n = 3):
    arrs = [[] for i in range(n)]
    
    current = 0
    dir = 1

    for i in range(len(M)):
        for j in range(n):
            if j == current:
                arrs[j].append(True)
            else:
                arrs[j].append("")
        current += dir
        if dir == 1 and current == n-1:
            dir = -1
        if dir == -1 and current == 0:
            dir = 1
    
    index = 0

    for i in range(n):
        for j in range(len(M)):
            if arrs[i][j]:
                arrs[i][j] = M[index]
                index += 1
    
    ret = ""
    current = 0
    dir = 1

    for i in range(len(M)):
        for j in range(n):
            if arrs[j][i]:
                ret += arrs[j][i]

    return ret
