def dat(data1):
    if len(data1) == len(set(data1)):
        return True
    else:
        return False


print(dat([1, 2, 2, 3]))
