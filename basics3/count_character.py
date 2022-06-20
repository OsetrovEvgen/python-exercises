import pandas as pd

def count(a):
    b = (pd.Series(list(a)).value_counts())
    return b

print(count('Write a Python program to count the number of each character of a given text of a text file'))

