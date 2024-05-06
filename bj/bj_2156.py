n = int(input())
data = list()

for i in range(n):
    data.append(int(input()))

res = [0] * n
res[0] = data[0]
if n > 1:
    res[1] = data[0] + data[1]
if n > 2:
    res[2] = max(data[2] + data[1], data[2] + data[0], res[1])

for i in range(3, n):
    res[i] = max(res[i-1], res[i-3] + data[i-1] + data[i], res[i-2] + data[i])

print(res[n-1])