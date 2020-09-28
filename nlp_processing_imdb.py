import pandas as pd

from nltk.tokenize import word_tokenize
from sklearn import linear_model
from sklearn import metrics
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":
    df = pd.read_csv("IMDB_Dataset.csv")

    # Map positive sentiment to 1 and negative to 0
    df.sentiment = df.sentiment.apply(lambda x: 1 if x == "positive" else 0)

    # Create a new column kfold and fill it with -1
    df["kfold"] = -1

    # Randomize the rows of data
    df = df.sample(frac = 1).reset_index(drop = True)

    # Get the labels
    y = df.sentiment.values

    # Initiate kfold class module
    kf = model_selection.StratifiedKFold(n_splits = 5)

    # Fill the new kfold column
    for f, (t_, v_) in enumerate(kf.split(X = df, y = y)):
        df.loc[v_, 'kfold'] = f

    for fold_ in range(5):
        train_df = df[df.kfold != fold_].reset_index(drop = True)
        test_df = df[df.kfold == fold_].reset_index(drop = True)

        count_vec = CountVectorizer(tokenizer = word_tokenize, token_pattern = None)

        # Fit the vectorizer with training data
        count_vec.fit(train_df.review)

        # Transform training and validation data
        xtrain = count_vec.transform(train_df.review)
        xtest = count_vec.transform(test_df.review)

        # Initialize and fit logistic regression model
        model = linear_model.LogisticRegression()
        model.fit(xtrain, train_df.sentiment)

        # Make predictions on test data
        predictions = model.predict(xtest)

        # Calculate accuracy
        accuracy = metrics.accuracy_score(test_df.sentiment, predictions)

        print("================")
        print(f"Fold : {fold_}")
        print(f"Accuracy : {accuracy}")

