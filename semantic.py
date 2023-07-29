# all of the code below has been copied from PDF file
import spacy

nlp = spacy.load('en_core_web_md')

print("EXAMPLE 1:")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

# interpret the  similarities between cat, monkey and banana
'''
'cat' and 'monkey' have the strongest similarity, model recognises that they are both animals. 
'banana' and 'money' are also similar, mokeys are often associated with bananas.
'cat' and 'banana' have the weakest similarity.
'''

#create my own example like the one above
print("MY EXAMPLE:")
word1 = nlp("kitten")
word2 = nlp("cub")
word3 = nlp("apple")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print("\n")

'''
'kitten' and 'cub' have a strong similarity, the machine recognises that they are both baby animals and both are part
of the feline family.
there is a very weak similaity between 'apple' and 'cub' as well as 'apple' and 'kitten', they are very different.
'''
print("EXAMPLE 2:")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print("\n")

print("EXAMPLE 3:")
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
print("\n")

# compare running the examply file with the model 'en_core_web_sm' and model 'en_core_web_md'
'''
The scores are much lower when the model 'en_core_web_sm' is running as there are no word vectors loaded on model. 
With the model 'en_core_web_md' running, the scores are much higher.
''' 