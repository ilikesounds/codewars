def increment_string(string):
    char = ''
    digit = ''
    for i, c in enumerate(string):
        if ord(c) >= 48 and ord(c) <= 57:
            digit += c
        else:
            char += c
    inc = ord(digit[-1:]) + 1
    digit = digit[:-1] + char(inc)
    ans = char + digit
    return ans
