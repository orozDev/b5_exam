# 2)zadacha

def texts(text):
    str = ""
    for char in text:
        if text.count(char.lower()) > 1:
            if char.islower():
                str += "("
            else:
                str += "["
        else:
            if char.islower():
                str += ")"
            else:
                str += "]"
    return str

print(texts("oroz"))  
print(texts("ORoz"))  
print(texts("OrOz"))  

# 50/50