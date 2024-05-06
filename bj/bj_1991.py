n = int(input())
lst = list()

for i in range(n):
    tmp = list(map(str, input().split()))
    lst.append(tmp)

def find(target):
    for idx in range(len(lst)):
        if lst[idx][0] == target:
            return idx

def left_search(node):
    print(node[0], end="")
    if node[1] != '.':
        pos = find(node[1])
        left_search(lst[pos])
    if node[2] != '.':
        pos = find(node[2])
        left_search(lst[pos])
    return

def mid_search(node):
    if node[1] != '.':
        pos = find(node[1])
        mid_search(lst[pos])
    print(node[0], end="")
    if node[2] != '.':
        pos = find(node[2])
        mid_search(lst[pos])
    return

def right_search(node):
    if node[1] != '.':
        pos = find(node[1])
        right_search(lst[pos])
    if node[2] != '.':
        pos = find(node[2])
        right_search(lst[pos])
    print(node[0], end="")
    return

left_search(lst[0])
print()
mid_search(lst[0])
print()
right_search(lst[0])
