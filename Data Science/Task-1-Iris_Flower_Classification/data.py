import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Iris.csv')

# X = df.drop('target_variable', axis=1)  # Features
# y = df['target_variable']               # Target variable

# Display only the headers
# print(df)
# print(df.shape)

df=df.drop(columns=["Id"])
# print(df)

# print(df.head()) #Return first 5 entries

df["Species"].replace({"Iris-setosa":1,"Iris-versicolor":2,"Iris-virginica":3},inplace=True)


x=pd.DataFrame(df,columns=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]).values
y=df.Species.values.reshape(-1,1)

# print(y)