import spacy

nlp = spacy.load("en_core_web_sm")

# define garden path sentences
gardenpathSentences = [
    "The complex houses married and single soldiers and their families.",
    "The old man the boat.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi.",]

# tokenise and perform NER on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("\n")
    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"Token: {token.text}, POS: {token.pos_}, Tag: {token.tag_}, Entity: {token.ent_type_}")

# look up and print the explanation of selected entities
print("\n")
entity_fac = spacy.explain("PER")
print("PER: " + (entity_fac))

entity_fac = spacy.explain("GPE")
print("GPE: " + (entity_fac))

'''
The first entity is PER which is named person or family. This does make sense as it is short for person.
The second entity is GPE which is countries, cities and states. This doesn't make sense, the word assoiaction is not
    as simple as with the PER entity.
'''
