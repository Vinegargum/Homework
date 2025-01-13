#Задача "Однокоренные"
def single_root_words(root_word, *other_words):
    same_words = []
    other_words_2 = []
    root_word = str.lower(root_word)
    for j in range (len(other_words)):
        other_words_2.append (str.lower(other_words[j]))
    other_words = tuple(other_words_2)
    for i in range(len(other_words)):
        if other_words[i] in root_word or root_word in other_words[i]:
                same_words.append (other_words[i])
    return same_words
print(single_root_words("ЛЕД", 'КОРЕНЬ', "ледяной", "ледЫШКА", "слово", "леД в стакане"))
