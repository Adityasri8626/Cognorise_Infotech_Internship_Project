# Importing the necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the files and saving them into train and test dataframes
train_data = pd.read_csv('/kaggle/input/bigmart-sales-data/Train.csv')
test_data = pd.read_csv('/kaggle/input/bigmart-sales-data/Test.csv')

# Displaying the shape of the two dataframes
print("Train Data Shape:", train_data.shape)
print("Test Data Shape:", test_data.shape)

# Displaying the first 10 rows of the train dataframe
print("First 10 rows of Train Data:")
print(train_data.head(10))

# Displaying the columns of the train dataframe
print("Train Data Columns:")
print(train_data.columns)

# Getting information about the dataset
print("Train Data Info:")
print(train_data.info())

# Checking for null values in the training data
print("Null Values in Train Data:")
print(train_data.isnull().sum())

# Comment on the missing values
print("\nWe see that some values of Item Size and Outlet Size are missing.")
print("Out of the various categories, we would be comparing sales of each item vs item characteristics.")
