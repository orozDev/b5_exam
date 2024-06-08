# //////////////////////////////////////////////////////////////////////////////////////////////
def find_uniq(arrey):
    counts = {}
    for num in arrey:
        counts[num] = counts.get(num, 0) + 1
    for num, count in counts.items():
        if count == 1:
            return num

print(find_uniq([1, 1, 1, 2, 1, 2]))  
print(find_uniq([0, 0, 0, 55, 0, 0])) 
# ///////////////////////////////////////////////////////
# def find_uniq(arrey):
#     for i in arrey:
#         if  ==  
# print(find_uniq([ 1, 1, "erbrbtr", 2, "qwerdg", 1 ],))