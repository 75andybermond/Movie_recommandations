import pandas as pd
import re

def replace_values(element):
    """
    Replaces NaN values with 0 and string values with 1
    """
    if pd.isna(element):
        return 0
    elif isinstance(element, str):
        return 1
    else:
        return element

def find_and_remove_outliers(df, column):
    """
    Finds and removes the outliers in a given column of a dataframe
    """
    # Calculate the interquartile range (IQR)
    Q1 = df[column].quantile(0.20)
    Q3 = df[column].quantile(0.85)
    IQR = Q3 - Q1

    # Find the lower and upper bounds of the outliers
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    # Find the number of outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    # Remove the found outliers
    df.drop(outliers.index, inplace=True)
    return df

def clean_names(element):
    if pd.isna(element):
        return "unknown"
    # Split the string into a list of names
    names_list = element.split(",")
    # Put the names in lower case
    names_list = [name.strip().lower() for name in names_list]
    names_list = ' '.join(names_list)
    return names_list
 

