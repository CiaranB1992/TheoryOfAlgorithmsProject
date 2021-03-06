from collections import Counter

words = []


def isAnAnagram(word, user):
    word_counter = Counter(word)
    input_counter = Counter(user)
    return all(count <= input_counter[key] for key, count in word_counter.items())

def getAnagrams(user):
    lister = [word for word in words if len(word) <= len(user) ]
    for item in lister:
        if isAnAnagram(item, user):
            yield item


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
    print(list(result))
    print(len(list(result)))