# 2


def s(q="oroz"):
    obj = {}
    text = ""
    text2 = q.upper()
    for i in q:
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1

    for i in q:
        a = i in text2
        if obj[i] >= 2:
            if not a:
                text += "("
            else:
                text += "["
        else:
            if not a:
                text += ")"
            else:
                text += "]"

    print(text)


print(s("ORoz"))
