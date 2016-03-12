import json
myfile = json.load(open('TestDuplicateFile', 'r'))
uniq = set()
for p in myfile:
if p in uniq:
    print "duplicate : " + p
    del p
else:
    uniq.add(p)
print uniq