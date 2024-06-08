# 3)zadacha

def func(str):
    length = len(str)
    if length == 0:
        return"no one likes this"
    elif length == 1:
        return f"{str[0]} likes this"
    elif length == 2:
        return f"{str[0]} and {str[1]} like this"
    elif length == 3:
        return f"{str[0]}, {str[1]} and {str[2]} like this"
    else:
        return f"{str[0]}, {str[1]} and {length-2} others like this"

print(func([]))                                      
print(func(["Alex", "Jacob", "Mark", "Max" , 'defsdf']))  
print(func(["Alex", "Jacob", "Mark"]))  
print(func(["Alex", "Jacob"]))  

