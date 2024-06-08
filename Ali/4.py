# ///////////////////4 Задание//////////////////////////
def devisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

print(devisors(12))
print(devisors(6))




