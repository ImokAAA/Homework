def split(st:str, sp = ' '):
    splited = []
    split = []
    c = 0
    sl = st
    for i in st:
        split.append(i)
        if i == sp or c == len(st)-1:
            splited.append(split)
            split = []
        c+=1
    print(splited)

split("shap*al*aq", '*')
