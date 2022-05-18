def get_digits(num):
    ans = []
    while num > 0:
        ans.append(num%10)
        num = (num - (num%10))/10
    return tuple(reversed(ans))

print(get_digits(14564))