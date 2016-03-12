# import permutations module
from itertools import permutations as prm

num_of_cases = int(raw_input("Input number of words needed to be unscrambled: "))
# take input
counter = 1
while counter <= num_of_cases:
   scrambled_word = list(str(raw_input("Input scrambled word: ")))

# empty lists that will be appended to later
   prm_list = []
   possible_words = []

# takes each permutation of the input and puts in a list
   for i in prm(scrambled_word):
      prm_list.append("".join(i))

   def check(x, y):

   # open list of words
      dictionary = file('Dictionary.txt')

      # check each line in the dictionary against each item
      # in the list of permutations and add it to another empty list if it's a match
      for line in dictionary:
         for i in x:
            if i+'\n' == line:
               y.append(i)


   check(prm_list, possible_words)

# delete duplicates
   possible_words = list(set(possible_words))

# print out possible words
   if len(possible_words) == 0:
      print ("No matches found")
   else:
      for i in possible_words:
         print ("Possible Word for Scrambled Word #") + str(counter) + ": " + i

# add to the counter
   counter+=1