# program to make user input a sentence and change each alternate character of string to UPPERCASE 

#user input
sentence = input("Please enter a sentece to covert: ")
final_sentence = "" # blank string to store string's 

for i in range(len(sentence)):
    
    if i % 2 == 1:
        final_sentence += sentence[i].upper() 

    else:
        final_sentence += sentence[i].lower()

print(final_sentence)


# program using same string as above and change each alternate word of string to UPPERCASE

# used Stack Overflow to help with method
# https://stackoverflow.com/questions/8452616/how-to-upper-case-every-other-word-in-string-in-python

def alternate_uppercase(s):
    i = 0
    list_of_words = s.split(' ')
    alternate_word = []
    for w in list_of_words:
        if i:
            alternate_word.append(w.upper())
        else:
            alternate_word.append(w)
        i = int(not i)
    return " ".join(alternate_word)

print(alternate_uppercase(sentence))