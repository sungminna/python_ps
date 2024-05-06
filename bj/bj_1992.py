n = int(input())
data = list()
for i in range(n):
    s = str(input())
    tmp = list()
    for j in range(n):
        tmp.append(int(s[j]))
    data.append(tmp)


def check(r, c, size):
    res = str()
    if size == 1:
        if data[r][c] == 0:
            return '0'
        if data[r][c] == 1:
            return '1'

    if size > 1:
        alz = 1
        alo = 1
        for i in range(size):
            for j in range(size):
                if (data[r + i][c + j] == 1):
                    alz = 0
                if(data[r+i][c+j] == 0):
                    alo = 0

        if alz == 1:
            return '0'
        elif alo == 1:
            return '1'
        else:
            res += '('
            res += check(r, c, size // 2)
            res += check(r, c + size // 2, size // 2)
            res += check(r + size // 2, c, size // 2)
            res += check(r + size // 2, c + size // 2, size // 2)
            res += ')'
            return res


ans = check(0, 0, n)
print(ans)