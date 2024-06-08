
# //////////////////////1 Задание ///////////////////
# def find_uniq(arr):
#     counts = {}
#     for num in arr:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
    
#     for key, value in counts.items():
#         if value == 1:
#             return key


# print(find_uniq([1, 1, 1, 2, 1, 1]))  
# print(find_uniq([0, 0, 0, 55, 0, 0]))  




# ........................варианть...............................
def find_uniq(arr):
   
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    

    for num, count in counts.items():
        if count == 1:
            return num


arr1 = [1, 1, 1, 2, 1, 1]
arr2 = [0, 0, 0, 55, 0, 0]

print(find_uniq(arr1))  
print(find_uniq(arr2)) 
