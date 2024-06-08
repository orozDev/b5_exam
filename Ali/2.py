# ///////////////////////2 Задание/////////////////////
def ali_text(text):
    ali_text = ""
    for abu in text:
        if text.lower().count(abu.lower()) > 1:
            ali_text += "(" if abu.islower() else "["
        else:
            ali_text += ")" if abu.islower() else "]"
    
    return ali_text


text1 = "oroz"
text2 = "ORoz"
text3 = "OrOz"

print(ali_text(text1))  
print(ali_text(text2))  
print(ali_text(text3))  
