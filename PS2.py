#PS 2
#lsit a word if it has a certain character 
wordsList=["animal", "candle", "architect", "window", "solos", "radar", "civic"]
 
def filterWords(wordsList,character):
    wordsList=["animal", "candle", "architect", "window", "solos", "radar", "civic"]
    character="a"
    for character in wordsList:
        wordsList.pop()
    print(wordsList)
filterWords(wordsList, "a")

#is it a symmetric word?
def is_symmetric_word(word):
    alpha1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha2 = 'zyxwvutsrqponmlkjihgfedcba'
    length = len(word)
    n = len(word) // 2
    for i in range(length // 2):
        if word[n] == word[len(word)-1-n]:
               wordsList.pop()
        print(word)
is_symmetric_word("civic")
