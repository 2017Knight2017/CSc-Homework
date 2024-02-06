a = list(map(int, input().split()))

b = [i for i in a if not i % 3]
c = [i for i in a if not i % 5]
print(b)
print(c)
print()

for i in range(len(b)-1):
    for j in range(len(b)-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print(b)

for i in range(len(c)-1):
    for j in range(len(c)-i-1):
        if c[j] < c[j+1]:
            c[j], c[j+1] = c[j+1], c[j]
print(c)
