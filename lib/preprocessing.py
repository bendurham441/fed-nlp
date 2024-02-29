
def process(raw_string, stemmer=None, drop_numbers=True, drop_punct=True, stopwords=None):
    from nltk import word_tokenize, wordpunct_tokenize
    from nltk.corpus import stopwords as nltkstops
    import string

    stopword_list = nltkstops.words('english')
    if stopwords != None:
        stopword_list = stopwords

    stopword_list.extend(['."', '--', ".''", 'i', 'don'])

    final = str(raw_string).lower()
    tokens = word_tokenize(final) if not drop_punct else wordpunct_tokenize(final)
    final = [word for word in tokens if word not in stopword_list]
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

    with open(bigrams_path) as bg_file:
        for bg in bg_file.readlines():
            bigrams.add(bg.strip())

    trigrams = set()

    with open(trigrams_path) as tg_file:
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


def enhance(string_col, bigrams_path, trigrams_path, dict_path, stemmer='porter'):
    from gensim.corpora import Dictionary
    
    bigrams, trigrams = setup_enhance(bigrams_path, trigrams_path)
    return string_col.map(lambda x : ngram_enhance)

def load_stopwords(path):
    stopwords = []
    with open(path, 'r') as f:
        stopwords.extend([line.strip() for line in f])
    return stopwords