MAX_LENGTH = 40 

def decorate_title(title):
    length = len(title)
    diff   = MAX_LENGTH - length
    diff   = int(diff / 2 - 1)
    if diff * 2 + length + 2 != MAX_LENGTH:
        additional = 1
    else:
        additional = 0
    print("#" * MAX_LENGTH)
    print("#" + " " * diff + title + " " * (diff + additional)+ "#")
    print("#" * MAX_LENGTH)
