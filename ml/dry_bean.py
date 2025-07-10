import pandas as pd
from sklearn import tree

data = pd.read_csv('ml/DryBeanDataset/Dry_Bean_Dataset.csv')

print(data.head())

model = tree.DecisionTreeClassifier()
X_df = data.iloc[:,:-1]
y_df = data.loc[:,'Class']