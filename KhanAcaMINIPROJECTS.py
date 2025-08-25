#AUGUST 24,2025

# Write a script that:## Reads a text file.## Counts total words.## Finds the longest and shortest words.
#
# Finds frequency of each word.

with open("test.txt") as f:

    text = f.read().split()
print('content of the text file: ', text)

print("total words in the file: ", len(text))

longest_word = text[0]
shortest_word = text[0]
word_count = {}
for word in text:
    if len(longest_word)<len(word):
        longest_word = word

    if len(shortest_word)>len(word):
        shortest_word = word

    if word in word_count:
        word_count[word] = word_count[word] + 1

    else:
        word_count[word] = 1

print("longest word in the file: ", longest_word, "\n", "length of the longest word: ", len(longest_word))
print("shortest word in the file: ", shortest_word, "\n", "length of the shortest word: ", len(shortest_word))
print("Count the word Frequency", word_count)

