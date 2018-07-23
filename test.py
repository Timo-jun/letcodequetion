a = 'abababa'
a = re.finditer('a', a)
for i in a:
    print(a.span)