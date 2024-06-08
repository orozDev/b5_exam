# 3)
def Facebook(masiv):
    str1 = ""
    if len(masiv) == 0:
        str1+= "no one likes this"
    elif len(masiv) == 1:
        str1 += f"{masiv[0]} likes this"
    elif len(masiv) == 2:
        str1 += f"{masiv[0]} and {masiv[1]} like this"
    elif len(masiv) == 3:
        str1 += f"{masiv[0]}, {masiv[1]} and {masiv[2]} like this"
    elif len(masiv) > 3:
        str1 += f"{masiv[0]}, {masiv[1]} and {len(masiv)-2} others like this"
    print(str1)
Facebook(["Alex", "Jacob", "Mark", "Max",])
