from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 1
# a
iris = load_iris()
print(iris['DESCR'])

# b
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# c
X = df.drop('target', axis=1)
y = df['target']

x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(X, y, test_size=0.3, random_state=42)

# d
dt_model_1 = DecisionTreeClassifier()
dt_model_1.fit(x_train_1, y_train_1)
y_pred_1 = dt_model_1.predict(x_test_1)

# 2
x_train_2, x_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.4, random_state=42)

dt_model_2 = DecisionTreeClassifier()
dt_model_2.fit(x_train_2, y_train_2)
y_pred_2 = dt_model_2.predict(x_test_2)

x_train_3, x_test_3, y_train_3, y_test_3 = train_test_split(X, y, test_size=0.2, random_state=42)

dt_model_3 = DecisionTreeClassifier()
dt_model_3.fit(x_train_3, y_train_3)
y_pred_3 = dt_model_3.predict(x_test_3)

# 3
rf_model_1 = RandomForestClassifier()  # RandomForest model 1
rf_model_1.fit(x_train_1, y_train_1)

rf_model_2 = RandomForestClassifier()  # RandomForest model 2
rf_model_2.fit(x_train_2, y_train_2)

rf_model_3 = RandomForestClassifier()  # RandomForest model 3
rf_model_3.fit(x_train_3, y_train_3)