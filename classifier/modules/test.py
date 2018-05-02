import pandas as pd
import sys
import numpy as np
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import CountVectorizer


def NaiveBayes(search):
	newsdata=pd.read_csv(r'/home/bhavikk/DjangoProjects/myapp/classifier/modules/uci-news-url.csv')
	X = newsdata['TITLE']
	vectorizer=CountVectorizer()
	c=vectorizer.fit_transform(X.astype('U'))
	# # print(c)
	# y = newsdata['CATEGORY'];
	# classifier = MultinomialNB()
	# #X_train,y_train,X_test,y_test=train_test_split(c,y,test_size=0.2)
	# classifier.fit(c,y)
	classifier=pickle.load(open("/home/bhavikk/DjangoProjects/myapp/classifier/modules/pickles/naivebayes.pickle","rb"));
	# from here the classfication of our data starts 
	
	urldata=pd.read_excel('/home/bhavikk/DjangoProjects/myapp/classifier/modules/write2cell.xlsx')
	X=urldata['url']
	df=[]
	index=0
	for i in X:
		df.append(X[index][31:-1]);
		index+=1
	print(len(df))
	example_count = vectorizer.transform(df)

	pred = classifier.predict(example_count)
	# pro=classifier.predict_proba(example_count)

	output=pd.DataFrame({"url":X,"category":pred})
	# print(search)
	result=[];
	for x in range(len(output)):	
		if(output['category'][x]==search):
			result.append(output['url'][x])
	print(output['category']);
	return result;

def RandomForest(search):
	newsdata=pd.read_csv(r'/home/bhavikk/DjangoProjects/myapp/classifier/modules/uci-news-url.csv')
	X = newsdata['TITLE']
	vectorizer=CountVectorizer()
	c=vectorizer.fit_transform(X.astype('U'))
	# print(c)
	# y = newsdata['CATEGORY'];
	# classifier=RandomForestClassifier(n_estimators=5,criterion='entropy')
	# #X_train,y_train,X_test,y_test=train_test_split(c,y,test_size=0.2)
	# classifier.fit(c,y)
	classifier=pickle.load(open("/home/bhavikk/DjangoProjects/myapp/classifier/modules/pickles/randomforest.pickle","rb"));

	# from here the classfication of our data starts 
	
	urldata=pd.read_excel('/home/bhavikk/DjangoProjects/myapp/classifier/modules/write2cell.xlsx')
	X=urldata['url']
	# print(X.describe())
	df=[]
	index=0
	for i in X:
		df.append(X[index][31:-1]);
		index+=1
	print(len(df))
	example_count = vectorizer.transform(df)

	pred = classifier.predict(example_count)
	# pro=classifier.predict_proba(example_count)

	output=pd.DataFrame({"url":X,"category":pred})
	# print(search)
	result=[];
	
	for x in range(len(output)):	
		if(output['category'][x]==search):
			result.append(output['url'][x])
	print(output['category']);
	
	return result;

def KNN(search):
	newsdata=pd.read_csv(r'/home/bhavikk/DjangoProjects/myapp/classifier/modules/uci-news-url.csv')
	X = newsdata['TITLE']
	vectorizer=CountVectorizer()
	c=vectorizer.fit_transform(X.astype('U'))
	# # print(c)
	# y = newsdata['CATEGORY'];
	# classifier = KNeighborsClassifier(n_neighbors = 5, weights='uniform', algorithm='auto')	#X_train,y_train,X_test,y_test=train_test_split(c,y,test_size=0.2)
	# classifier.fit(c,y)
	classifier=pickle.load(open("/home/bhavikk/DjangoProjects/myapp/classifier/modules/pickles/knn.pickle","rb"));

	# from here the classfication of our data starts 
	
	urldata=pd.read_excel('/home/bhavikk/DjangoProjects/myapp/classifier/modules/write2cell.xlsx')
	df=[]
	index=0
	for i in X:
		df.append(X[index][31:-1]);
		index+=1
	print(len(df))
	example_count = vectorizer.transform(df)
	# print(X.describe())
	
	pred = classifier.predict(example_count)
	# pro=classifier.predict_proba(example_count)

	output=pd.DataFrame({"url":X,"category":pred})
	# print(search)
	result=[];
	for x in range(len(output)):	
		if(output['category'][x]==search):
			result.append(output['url'][x])
	print(output['category']);
	return result;