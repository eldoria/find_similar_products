from config import *

tags_en = {
    'ADJ': 'adjective',
    'ADP': 'adposition',
    'ADV': 'adverb',
    'AUX': 'auxiliary verb',
    'CONJ': 'coordinating conjunction',
    'DET': 'determiner',
    'INTJ': 'interjection',
    'NOUN': 'noun',
    'NUM': 'numeral',
    'PART': 'particle',
    'PRON': 'pronoun',
    'PROPN': 'proper noun',
    'PUNCT': 'punctuation',
    'SCONJ': 'subordinating conjunction',
    'SYM': 'symbol',
    'VERB': 'verb',
    'X': 'other'
}

tags_fr = {
    'ADJ': 'adjectif',
    'ADP': 'position',
    'ADV': 'adverbe',
    'AUX': 'verbe auxiliaire',
    'CONJ': 'conjonction de coordination',
    'DET': 'déterminant',
    'INTJ': 'interjection',
    'NOUN': 'nom',
    'NUM': 'numérique',
    'PART': 'particule',
    'PRON': 'pronom',
    'PROPN': 'nom propre',
    'PUNCT': 'ponctuation',
    'SCONJ': 'conjonction de subordination',
    'SYM': 'symbole',
    'VERB': 'verbe',
    'X': 'autre'
}

# permet de déterminer la composition d'une phrase
# pas terrible
def print_composition(p):
    print(p)
    sentence_composition = ''
    for token in nlp(p):
        sentence_composition += f'{tags_fr[token.pos_]} / '
    print(sentence_composition)


'''
product_1 = "Jus de poire"
product_2 = "Jus de pomme"
product_3 = "Jus de tomate"
product_4 = "Nectar de banane Franprix 1 L"
product_5 = "Nectare de banane 1 L"
product_6 = "Nectare de banane"
product_7 = "de Nectare banane"

print_similarity(product_1, product_2)
print_similarity(product_2, product_3)
print_similarity(product_3, product_4)
print_similarity(product_4, product_5)
print_similarity(product_4, product_6)
print_similarity(product_4, product_7)

print_composition(product_1)
'''
