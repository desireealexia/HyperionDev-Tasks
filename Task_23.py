# Little Sister's Vocabulary Challenge (https://exercism.org/tracks/python/exercises/little-sisters-vocab)

# Asingment 1 - function that takes given word and adds the 'un' prefix
# word (str): containg the root word
# return (str): root word with 'un' prefix
def add_prefix_un(word):
    return 'un'+ word

word = 'happy'
print(add_prefix_un(word))

# Assignment 2 - function transforms a list containg a prefix and words into a string with the prefix by the word
# vocab_words (list): list of vocabulary words
# prefix (str): prefix in first index of list
# return (str): prefix followed by vocabulary words with prefix applied, each word seperated by '::'
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    return prefix + ' :: ' + ' :: '.join(prefix+word for word in vocab_words[1:])

vocab_words = ['en', 'close', 'joy', 'lighten']
print(make_word_groups(vocab_words))

# Assignment 3 - function removes the suffix from the word
# word (str): word to remove suffix from
# return (str): word with suffix removed and spelling adjusted
def remove_suffix_ness(word):
    root = word[:-4]
    return root if root[-1] != 'i' else root[:-1]+'y'

word = 'sadness'
print(remove_suffix_ness(word))

# Assingment 4 - function changes the adjective within the sentence to a verb

# sentence (str): that uses the word in sentence
# index (int): index of the word to remove and transform
# return (str): word that changes the extracted adjective to a verb

def adjective_to_verb(sentence, index):
    verb = sentence.split(' ')[index]
    return verb[:-1] + 'en' if verb[-1] == '.' else verb + 'en'

sentence = 'It got dark as the sun set'
print(adjective_to_verb(sentence, 2))
