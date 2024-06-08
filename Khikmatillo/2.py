def povtor(string):
    a = ""
    for i in string:
        if string.count(i.lower()) > 1:
            if i.islower():
                a += "("
            else:
                a += "["
        else:
            if i.islower():
                a += ")"
            else:
                a += "]"
    return a
print(povtor("OROZ"))  

# 50/50