import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import train_test_split
from scipy.stats import linregress


def regression(search):
	data=pd.read_csv("./linearReg_data.csv")
	df_x=pd.DataFrame(data,columns=[" num_hrefs"," num_imgs"," num_videos"])
	df_y=data["shares"]
	df_x.fillna(0)
	df_y.fillna(0)
	reg=linear_model.LinearRegression()
	# x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
	reg.fit(df_x,df_y)
	d={' num_hrefs':'1',' num_imgs':'2',' num_videos':'3'}
	df=pd.DataFrame(data=d)
	# a=reg.predict(pd.DataFrame())
	a=reg.predict(df)
	print("result "+a)
	linregress(df_x,df_y)
	a=reg.predict(x_test)

