## NLP_IMDB

This problem is solved using Kaggle data for IMDB movie review set.
The data can be downloaded from the location 
https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

* Execution Output with CountVectorizer and Linear Regression

```
================
Fold : 0
Accuracy : 0.8908
================
Fold : 1
Accuracy : 0.8943
================
Fold : 2
Accuracy : 0.8933
================
Fold : 3
Accuracy : 0.8948
================
Fold : 4
Accuracy : 0.8906

Accuracy reached 89%
```
* Execution Output with CountVectorizer and Naive-Bayes algorithm
```
Using Naive Bayes Model
================
Fold : 0
Accuracy : 0.8466
Using Naive Bayes Model
================
Fold : 1
Accuracy : 0.8478
Using Naive Bayes Model
================
Fold : 2
Accuracy : 0.8373
Using Naive Bayes Model
================
Fold : 3
Accuracy : 0.8423
Using Naive Bayes Model
================
Fold : 4
Accuracy : 0.8482
```
* Using tfidf vectorizer along with ngram for Naive-Bayes
```
Using tfidf vectorizer with ngram
Using Naive Bayes Model
Using Naive-Bayes Algorithm...
================
Fold : 0
Accuracy : 0.892
Using tfidf vectorizer with ngram
Using Naive Bayes Model
Using Naive-Bayes Algorithm...
================
Fold : 1
Accuracy : 0.8897
Using tfidf vectorizer with ngram
Using Naive Bayes Model
Using Naive-Bayes Algorithm...
================
Fold : 2
Accuracy : 0.8902
Using tfidf vectorizer with ngram
Using Naive Bayes Model
Using Naive-Bayes Algorithm...
================
Fold : 3
Accuracy : 0.8899
Using tfidf vectorizer with ngram
Using Naive Bayes Model
Using Naive-Bayes Algorithm...
================
Fold : 4
Accuracy : 0.8897
```
