
def process(raw_string, stemmer=None, drop_numbers=True):
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    import string

    final = str(raw_string).lower()
    tokens = word_tokenize(final)
    final = [word for word in tokens if word not in stopwords.words('english')]
    if drop_numbers:
        final = [token for token in final if not token.isnumeric()]
    if stemmer:
        stemmed = [stemmer.stem(token) for token in final]
        final = stemmed
    final = [token for token in final if token not in string.punctuation]
    return final