# 2)
def func(str1):
    a = []
    b = ""
    for i in str1:
        a.append(i)
    for i in a:
        if type(i) == str:
            if i.islower():
                if a.count(i) >1:
                    b +="("
                elif a.count(i) == 1:
                    b +=")"
            elif i.isupper():
                if a.count(i) >1:
                    b +="["
                elif a.count(i) == 1:
                    b +="]"
    print(b)
func(input())

# 50/50