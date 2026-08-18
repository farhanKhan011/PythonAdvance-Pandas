# -------Pandas Cleaning Wrong Formate-----------

'''
Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
Convert Into a Correct Format
In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:
'''
# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:
# import pandas as pd 
# df = pd.read_csv("CleaningData/WrongFormateData.csv")
# df["Date"] = pd.to_datetime(df["Date"], format ='mixed')
# print(df.to_string())
# in the output  the date in row 26 was fixed,
#  but the empty date in row 22 got a NaT (Not a Time) value,
#  in other words an empty value. One way to deal with empty values is simply removing the entire row.

'''
Removing Rows
The result from the converting in the example above gave us a NaT value, which can be handled as a NULL value, and we can remove the row by using the dropna() method.
'''
# Remove rows with a NULL value in the "Date" column:
# import pandas as pd 
# df = pd.read_csv("CleaningData/wrongFormateData.csv") 
# df["Date"] = pd.to_datetime(df["Date"] , format="mixed")
# df.dropna(subset=["Date"],inplace = True)
# print(df.to_string())

# --------Cleaning Wrong Format Data Completed------
