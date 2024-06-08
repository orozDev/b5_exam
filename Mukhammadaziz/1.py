# 1
nums = [1,1,1,2,1,1] # 2

def s():
    obj = {}
    for i in nums:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    for i in obj:
        if obj[i] == 1:
            return i

print(s())