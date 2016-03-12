outfile = open('stripOutfile.txt', 'w')
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a="hello are you how are hello hello helo"
a=' '.join(unique_list(a.split()))
outfile.write(line.split(None, 1)[0])
print(a)