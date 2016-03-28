To Run this project:
Run FinProject.py in console and ensure that the dictionary file is in the same diretory as this
program.

I have a few programs contained in my github repository and i am going to discuss each of them below.

FinProjectpy:

This is the finished and final solution.
There are three main methods in this program, IsAnAnagram
getAnagrams and Run.

IsAnAnagram: takes the input to the user and checks it against all words
that the letters can rearrange into. It uses counters to store the input and output 
the words and I use these as a control to shape the length and ammount of words
returned in the output.
return all(count <= input_counter[key] for key, count in word_counter.items()) in IsAnAnagram 
is the line of code that sorts all of the letters returned and prepares them for organisation in the
following method.

GetAnagrams:
This method organises and passes on all found anagrams to the run method. This method takes the 
results from IsAnAnagram and sorts them in preparation for following sorting and output.

Run:
This method begins by opening the dictionary file and reads in the texxt ready to parse it for the pervious methods.
The first user required field is the "enter word2 which then puts the user input and returns it to the getAnagrams
method. The for loop here ensures that the only output from the program is a list of the longest or
tied for longest words contained inside the dictionary text file.
The folowing forloop prints out the list that was found to be of maxlength.

I Timed the program with the timeit function but the only problem i came across with this method was
that it started the timer as soon as the program ended, it doesnt only record how long it takes to
find the list of words but also times the ammount of time for user input. This is inefficient but
I ran out of time before i could find a more efficent way of timing the runTime.

Remove Diplicates:
This was a progam i made to remove duplicate words from the text file. I created this profile because 
the dictionary file i found was too small for this project, so i copy and pasted words from all
sorts of files from the internet into the dictionary file, then stripped all duplicates using this method.

Contains:
This was to test whether or not a string would contain the words listed. This idea ran into a dead end so 
I did not include that method of outputting contained words in my final product.

StripAndOutput + StripFile:
These were made to strip all but the first words on each line ( for the purpose of stripping definitions
from the dictionary file and only including a single word per line) The StripAndOutput only differs
from StripFile in the form of outputting to a new textfile.

AnaTest0-4:
The AnaTest files from AnaTest to AnaTest4 were the gradual improvements i was making to my program over time.
The original program i began with was Garret Jordans Conundrum2 that was uploaded to your gitHub 
page. I also got help from posting and reviewing questions on stack overflow. I will provide
links below.

http://stackoverflow.com/questions/35901307/python-strings-and-anagrams
http://stackoverflow.com/questions/35880298/python-strings-with-anagrams
http://stackoverflow.com/questions/35880298/python-strings-with-anagrams

