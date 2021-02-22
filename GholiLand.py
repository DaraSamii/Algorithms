n,q = map(int, input().split(' '))

ns = list(map(int, input().split(' ')))

qs = []
for i in range(q):
    qs.append(int(input()))

for i in qs:
    result = 0
    for j in ns:
        if i > j:
            result += 1
    print(result)