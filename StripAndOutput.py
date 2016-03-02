WordList = []
outfile = open('stripOutfile.txt', 'w')
with open('StripTest.txt','r') as f:
            for line in f:
                outfile.write(line.split(None, 1)[0])
                outfile.write('\n')
capacity = len(WordList)
index = 0
while index!=capacity:
    line = WordList[index]
    print(WordList[index])
    index = index+1