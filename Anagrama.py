word = input("Insert a word: ")
word1 = input("Insert another word: ")

# La función sorted permite que los carácteres se ordenen alfabeticamente
def anagram(word, word1):
    word = sorted(word)
    word1 = sorted(word1)
    
    return word == word1


if word == word1:
    print("Is not anagram")
else:
    r = anagram(word, word1)

if r:
    print("¡Is anagram!")
else:
    print("¡Is not anagram!")
