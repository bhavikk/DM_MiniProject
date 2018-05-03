import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
def spamClassify():
    data = pd.read_csv('./spam.csv', engine='python')
    data = data.applymap(lambda x: x.encode('unicode_escape').
                         decode('utf-8') if isinstance(x, str) else x)
    # print(data.columns)
    X = data['v2']
    y = data['v1']
    # print(X)
    sampleData = pd.DataFrame({'text': X, 'category': y})

    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(X.astype('U'))
    targets = y;
    classifier = MultinomialNB()
    classifier.fit(counts, targets)
    example = ['are you free tonight?']
    #
    example_count = vectorizer.transform(example)

    pred = classifier.predict(example_count)
    print(pred)

def docclassify():
    newsdata=pd.read_csv('./datasetConverted.csv', engine='python',encoding = "ISO-8859-1")
    # newsdata = newsdata.applymap(lambda x: x.encode('unicode_escape').
    #                      decode('utf-8') if isinstance(x, str) else x)

   # print(news)
    news = newsdata['news']
    count_vect=CountVectorizer()
    c=count_vect.fit_transform(news)
    targets = newsdata['type'];
    classifier = MultinomialNB()
    classifier.fit(c, targets)
    urldata=pd.read_excel('./write2cell.xlsx')
    X=urldata['url']
    X=X[:20]
    print(X.describe())
    example_count = count_vect.transform(X)

    pred = classifier.predict(example_count)
    # pro=classifier.predict_proba(example_count)
    output=pd.DataFrame({"url":X,"category":pred})
    print(output)



docclassify()
