# 4
def s(n):
    if n == 0:
        return 0
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    return arr


print(s(10))

# 50/50