# 4)
def Devisors(n):
    a = []
    for i in range(n,0,-1):
        if n %i == 0:
            a.append(i)
    a.reverse()
    print(a)
Devisors(int(input()))