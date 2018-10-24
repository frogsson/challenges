#!/usr/bin/python3
import argparse
import random
import json
import os
import sys


# TODO
# add a proper 'first_word' state
# add 2 < word states in dict 
# add a probability to 'length' with exponential growth since it's a markov chain

# dict structure
# {"word": {"prob": {"probability_word": 100}, count: 100}}

def generate_dict(input_text, output_dict):
    with open(input_text, 'r') as f:
        text = f.read()

    # punctations = '?!.,'
    for char in text:
        if not char.isalpha() and char is not ' ':
            text = text.replace(char, '')

    text = text.lower().split(' ')

    words = {}
    for num, word in enumerate(text):
        if word not in words:
            words[word] = {} 
            words[word]['prob'] = {} 
            words[word]['count'] = 1
        else:
            words[word]['count'] += 1

        if num + 1 < len(text) and text[num + 1] not in words[word]:
            # if "probability word" not found create entry 
            words[word]['prob'][text[num + 1]] = 1
        elif num + 1 < len(text) and text[num + 1] in words[word]:
            # elif "probability word" already found add another to existing entry
            words[word]['prob'][text[num + 1]] += 1

    output_dict = 'dicts/%s.json' % (output_dict)
    with open(output_dict, 'w') as f:
        f.write(json.dumps(words))


def generate_sentence(input_dict):
    if not input_dict.endswith('.json'):
        input_dict = '%s.json' % input_dict

    input_dict = 'dicts/%s' % input_dict

    with open(input_dict, 'r') as f:
        words = json.loads(f.read())

    sentence = ''
    first_word = True
    length = random.randrange(5, 20) # temporary
    current_word = ''

    for _ in range(length): 
        if first_word:
            pop = []
            weight = []
            for word, prob in words.items():
                pop.append(word)
                weight.append(prob['count'])
            current_word = random.choices(pop, weight, k=1)[0]
            sentence = current_word if len(sentence) is 0  else '%s %s' % (sentence, current_word)
            first_word = False
        else:
            pop = []
            weight = []
            for word, prob in words[current_word]['prob'].items():
                pop.append(word)
                weight.append(prob)

            if len(pop) > 0:
                current_word = random.choices(pop, weight, k=1)[0]
                sentence += ' %s' % current_word
            else:
                first_word = True

    return sentence


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--new',
                        nargs=2,
                        metavar=('input', 'output'),
                        help='generate a new dictionary from a textfile')
    parser.add_argument('-g', '--generate',
                        metavar=('dictname'),
                        help='generate a sentence from choosen dictionary')
    parser.add_argument('-l', '--list',
                        action = 'store_true',
                        help='list existing dictionaries')

    args = parser.parse_args()

    if args.generate:
        print(generate_sentence(args.generate))
    elif args.new:
        generate_dict(args.new[0], args.new[1])
    elif args.list:
        print(os.listdir('dicts'))
    else:
        print('main.py -h')


if __name__ == "__main__":
    main()
