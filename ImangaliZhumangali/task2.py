def most_common_words(filepath, number_of_words=3):
    with open(filepath) as f:
        file_content = f.read()
    
    dic = {}
    file = file_content.lower().split()
    for item in file:
        if '.' in item or ',' in item:
            item = item[:-1]
        if item in dic.keys():
            dic[item]+=1
        else: dic[item] = 1
    ans = []
    for i in range(number_of_words):
        key = max(dic, key=dic.get)
        ans.append(key)
        del dic[key]
    return ans

print(most_common_words("/home/imangali/python_found_epam/Homework/data/lorem_ipsum.txt"))