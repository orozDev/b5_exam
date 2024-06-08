# 1)zadacha

def find_uniq(arr):
    sort = sorted(arr)
    
    if sort[0] != sort[1]:
        return sort[0]
    else:
        return sort[-1]

print(find_uniq([1, 1, 1, 2, 1, 1])) 
print(find_uniq([0, 0, 0, 0, 0, 0]))  

# 50/50