
def process(raw_string, stemmer=None, drop_numbers=True, drop_punct=True):
    from nltk import word_tokenize, wordpunct_tokenize
    from nltk.corpus import stopwords
    import string

    final = str(raw_string).lower()
    tokens = word_tokenize(final) if not drop_punct else wordpunct_tokenize(final)
    final = [word for word in tokens if word not in stopwords.words('english')]
    if drop_numbers:
        final = [token for token in final if not token.isnumeric()]
    if stemmer:
        stemmed = [stemmer.stem(token) for token in final]
        final = stemmed
    final = [token for token in final if token not in string.punctuation]
    return final


def setup_enhance(bigrams_path, trigrams_path):
    import os
    bigrams = set()

    with open(os.path.join('ngrams', 'bigrams')) as bg_file:
        for bg in bg_file.readlines():
            bigrams.add(bg.strip())

    trigrams = set()

    with open(os.path.join('ngrams', 'trigrams')) as tg_file:
        for tf in tg_file.readlines():
            trigrams.add(tf.strip())

    return bigrams, trigrams

def ngram_enhance(raw_string, bigrams, trigrams):
    to_add = []
    raw_string = str(raw_string)
    for bg in bigrams:
        if str(bg) in raw_string.lower():
            to_add.append('_'.join(bg.split(' ')))
    for tg in trigrams:
        if str(tg) in raw_string.lower():
            to_add.append('_'.join(tg.split(' ')))

    return raw_string + ' ' + ' '.join(to_add)