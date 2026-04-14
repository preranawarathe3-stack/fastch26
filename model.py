from sklearn.datasets import load_iris

from sklearn.linear_model import LogisticRegression

import joblib

from sklearn.model_selection import train_test_split

iris = load_iris()
X= iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

lg = LogisticRegression()
lg.fit(X_train,y_train)

joblib.dump(lg,"mymodel")
