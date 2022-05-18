def is_polindrome(st):
    for i in range(int(len(st)/2)):
        if(st[i] != st[len(st)-i-1]):
            return False
    return True

st1 = "racecar"
st2 = "asdfd"

print(st1)
print(is_polindrome(st1))

print(st2)
print(is_polindrome(st2))