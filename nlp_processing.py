from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize

# Create a corpus of sentences
corpus = [
    "hello, how are you?",
    "I'm getting bored at home, What about you? What do you think?",
    "are you interested in playing a game",
    "let's see if this works!"
    "YES!!!!"
]

# Initialize CountVectorizer
#cnt_vec = CountVectorizer()

# Initialize CountVectorizer with word_tokenize from nltk as tokenizer
cnt_vec = CountVectorizer(tokenizer = word_tokenize, token_pattern = None)

# Fit the vectorizer on corpus
cnt_vec.fit(corpus)

corpus_transformed = cnt_vec.transform(corpus)
print(corpus_transformed)
print(cnt_vec.vocabulary_)
