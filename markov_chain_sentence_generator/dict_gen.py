#!/usr/bin/python3


# {"word": {"probability_word": 100}}
with open('generic.txt', 'r') as f:
    text = f.read()

punctation = '?!.,'
for char in text:
    if not char.isalpha() and char is not ' ':
        text = text.replace(char, '')

text = text.split(' ')

words = {}
for num, word in enumerate(text):
    if num + 1 < len(text):
        print(num, word, text[num + 1])
    else:
        print(num, word, "EOL")

    if word not in words:
        words[word] = {} 


    if num + 1 < len(text) and text[num + 1] not in words[word]:
        # if "probability word" not found create entry 
        words[word][text[num + 1]] = 1
    elif num + 1 < len(text) and text[num + 1] in words[word]:
        # elif "probability word" already found add another to existing entry
        words[word][text[num + 1]] += 1

print(words)
