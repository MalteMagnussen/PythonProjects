from sklearn.feature_extraction.text import CountVectorizer


with open(r"moby_dick.txt", encoding="utf-8") as f:
    corpus = [f.read()]
    vectorizer = CountVectorizer()

    fit = vectorizer.fit_transform(corpus)
    print(type(fit))
    res = fit.todense()  # returns a numpy array of same shape"
    document_idx = vectorizer.vocabulary_["wood"]
    document_count = sum(
        res[:, document_idx]
    )  # sum all row cells where column == index
    print("document occurs {} times in the text".format(document_count))

    # corpus.close()
