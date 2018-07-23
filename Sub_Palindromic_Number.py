def sub_palindromic_number(s):
    a, b = '', ''
    i = 0
    while i < len(s):
        c = s.rindex(s[i])
        if c != -1:
            a = s[i:c+1]
            if a == a[::-1]:
                b = a
                i = c
        i += 1
    return b

