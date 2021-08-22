#  ACTIVIDAD: Single Words - 22/08/2021

#  INSTRUCCIONES: Your task is to remove all duplicate words from a string,
#  leaving only single (first) word entries.
#  Input: 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
#  Output: 'alpha beta gamma delta'
#  This algoritm must run in time n.


def singleWords(words):

    wordsDictionary = {}

    words = words.split(" ")
    for word in words:
        wordsDictionary[word] = None
    return " ".join(wordsDictionary.keys())


print(singleWords(
    'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
