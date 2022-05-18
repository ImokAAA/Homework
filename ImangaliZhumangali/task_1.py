def magic(st):
    count = 0
    for i in st:
        if(i == "\""):
            st = st[:count] + "\'" + st[count+1:]
        elif(i == "\'"):
            st = st[:count] + "\"" + st[count+1:]
        count += 1
    return st

st = "asd\"afdadf\'\'adf"
print(st)
print(magic(st))