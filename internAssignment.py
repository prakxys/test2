#!python 3

#Program to count occurrences of "the", the letter "e", total number of lines in the file, and size of the file.
#extra credit - change the word "the" to "_the_"

import os
import re


#identify and count "the"
wordCounter = open("sample_text.txt","r").read().lower()
theCounter = re.split(r"\W+?", wordCounter)
print(theCounter.count("the"))



#Identify and count the letter "e"

letter = "e"dfd

count = wordCounter.count(letter)
print("number of e's are " +str(count))




#Count the total number of lines in the file
lineCount = 1
with open("sample_text.txt","rb") as f:
    for line in f:
        lineCount+=1df
print (str(lineCount) + " lines")


asdf
asdf
asdf
a
#Identify the total size of the file

totalSize = os.path.getsize("sample_text.txt")
print(str(totalSize) + " bytes")
df


#Change the word "the" to "_the_"
asdfasdf


asgasdg
asgasdgx
