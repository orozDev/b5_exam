def shifr_text(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    

    result = []


    for char in text: 
        if char.islower():
            if counts[char] > 1:
                result.append('(')
            else:
                result.append(')')
        elif char.isupper():
            if counts[char] > 1:
                result.append('[')
            else:
                result.append(']')
    
    return ''.join(result)




print(shifr_text("oroz")) 
print(shifr_text("ORoz")) 
print(shifr_text("OrOz")) 

    