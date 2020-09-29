from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

# Stemming and lemmatization reduce a word to smallest form
# Using the most common Snowball Stemmer and WordNetLemmatizer

# Word corpus
words = ['play', 'plays', 'player', 'played', 'playing']

# Initialize Stemmer
stemmer = SnowballStemmer('english')

#Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

for word in words:
    print("===================")
    print(f"Word = {word}")
    print(f"Stemmed Word = {stemmer.stem(word)}")
    print(f"Lemmatized Word = {lemmatizer.lemmatize(word)}")
