# 3

arr = ["Alex", "Jacob", "Mark", "Max", "Mark", "Max"]


def s(n):
    if len(arr) == 0:
        return "no one likes this"
    elif len(arr) == 1:
        return f"{arr[0]} likes this"
    elif len(arr) == 2:
        return f"{arr[0]} ans {arr[1]} likes this"
    elif len(arr) == 3:
        return f"{arr[0]}, {arr[1]} and {arr[2]} likes this"
    elif len(arr) > 3:
        a = len(arr) - 2
        return f"{arr[0]}, {arr[1]} and {a} others likes this"


print(s(arr))