# ----------Pandas - Cleaning Empty Cells-----------

'''
Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''
# Return a new Data Frame with no empty cells:

# import pandas as pd 
# df = pd.read_csv("CleaningData/data.csv")
# newdf = df.dropna()
# print(newdf.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
# If you want to change the original DataFrame, use the inplace = True argument:

# Remove all rows with NULL values:
# import pandas as pd 
# df = pd.read_csv("CleaningData/data.csv")
# df.dropna(inplace=True)
# print(df.to_string())

'''
Note: Now, the dropna(inplace = True) will NOT return a new DataFrame,
but it will remove all rows containing NULL values from the original DataFrame.
'''
'''
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:
'''
# Replace NULL values with the number 130:
# import pandas as pd 
# df = pd.read_csv("CleaningData/data.csv")
# df.fillna(130, inplace= True)
# print(df)

'''
Replace Only For Specified Columns
The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:
'''
# Replace NULL values in the "Calories" columns with the number 130:
# import pandas as pd
# df = pd.read_csv('data.csv')
# df.fillna({"Calories": 130}, inplace=True)

'''
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

Example
'''
# Calculate the MEAN, and replace any empty values with it:
# import pandas as pd

# df = pd.read_csv('CleaningData/data.csv')
# x = df["Calories"].mean()
# df.fillna({"Calories":x}, inplace = True)
# print(df.to_string())
# Mean = the average value (the sum of all values divided by number of values).

''' 
Calculate the MEDIAN, and replace any empty values with it: 
'''
# import pandas as pd
# df = pd.read_csv("CleaningData/data.csv")
# x = df["Calories"].median()
# df.fillna({"Calories":x} , inplace = True)
# print(df.to_string())
# Median = the value in the middle, after you have sorted all values ascending.

'''
Mode = the value that appears most frequently.
Calculate the MODE, and replace any empty values with it:
'''
# import pandas as pd
# df = pd.read_csv("CleaningData/data.csv")
# x = df["Calories"].mode()[0]
# df.fillna({"Calories":x}, inplace = True)
# print(df.to_string())

# -----CleaningEmptyCells Completed--------
