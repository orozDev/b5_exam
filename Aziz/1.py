def find_uniq(arr):
    a, b, c = arr[:3]
    if a == b:
        uniq = a
    elif a == c:
        return b
    else:
        return a
    
    for num in arr:
        if num != uniq:
            return num

print(find_uniq([1, 4, 1, 1, 1]))