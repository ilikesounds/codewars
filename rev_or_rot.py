def revrot(strng, sz):
    if sz <= 0 or sz > len(strng):
        return ""
    else:
        new_list = map(''.join, zip(*[iter(strng)]*sz))
        new_list = list(new_list)
        new_str = ''
        for i in new_list:
            cube = 0
            for n in i:
                cube += int(n)**3
            if cube % 2 == 0:
                new_str += i[::-1]
            else:
                i = i + i[0]
                i = i[1:]
                new_str += i
    return new_str
