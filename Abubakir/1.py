# 1)
def find_uniq(masiv):
    for i in masiv:
        if masiv.count(i)==1:
            return i
    else:
        print("est tolka pahojie")
res = find_uniq([ 1, 1, 1, 1, 1, 1, 2, 11, 12, 32, 32, 32])

print(res)