from collections import Counter
import operator
words = []


def isAnAnagram(word, user):
    word_counter = Counter(word)
    input_counter = Counter(user)
    return all(count <= input_counter[key] for key, count in word_counter.items())

def getAnagrams(user):
    content = []
    lister = [word for word in words if len(word) <= len(user) ]
    for item in lister:
        if isAnAnagram(item, user):
            content.append(item)

    return content


with open('Dictionary.txt', 'r') as f:
    allwords = f.readlines()
f.close()

for x in allwords:
    x = x.rstrip()
    words.append(x)
inp = 1


while inp != "99":
    inp = input("enter word:")
    result = getAnagrams(inp)
    
    length = 0
    maxlength = 0
    for word in result:
        length = len(word)
        if length > maxlength:
            maxlength = length
        else:
            pass

    for i in result:
        if len(i) is maxlength:
            print(i)
        else:
            pass

    print(maxlength) 
    #print(result) #uncomment to output all words contained in the dictionary file that match the user string

