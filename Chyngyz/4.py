# 4)zadacha 

def devisors(n):

    massiv = []
    for i in range(1, n + 1):

        if n % i == 0:
            massiv.append(i)
    return massiv

print(devisors(12)) 
print(devisors(6))   
print(devisors(16))  
 