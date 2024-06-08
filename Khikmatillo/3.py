def zad4(users):
    a = 0 
    b = users[0]
    c=users[1]
    d=users[2]
    for i in users:
        a=a+1
    if a <=0:
       print(f"{b} {c}, like this")
    elif a <= 5:
         print(f"{b} {c} and {d} like this")
    else:
        print(f"{b} {c}, and {a-2} others like this")   
zad4([])

# 50/50 x