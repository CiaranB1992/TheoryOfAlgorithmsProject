WordList = []
with open('StripTest.txt','r') as f:
            for line in f:
                WordList.append(line.split(None, 1)[0])
capacity = len(WordList)
index = 0
while index!=capacity:
    line = WordList[index]
    print(WordList[index])
    index = index+1

outfile = open('stripOutfile.txt', 'w')
outfile.write(l.split()[-1] + '\n')

infile.close()
outfile.close()