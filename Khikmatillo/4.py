def zad4(chislo):
    a = []
    for i in range(1, chislo + 1):
        if chislo % i == 0:
            a.append(i)
    return a
print(zad4(10)) 
print(zad4(30))  