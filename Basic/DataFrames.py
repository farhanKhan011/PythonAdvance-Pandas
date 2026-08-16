# ------------DataFrames-----------

'''
What is a DataFrame?
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
'''
# Create a simple Pandas DataFrame:
# import pandas as pd
# food = {
#     "fruits":["apples","bananas","grapes"],
#     "dryFruits":["nuts","wallnut","almonds"]
# }
# x = pd.DataFrame(food)
# print(x)
'''
Locate Row:
As you can see from the result above, the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
Example
Return row 0:
'''
# print(x.loc[0])
# Note: This example returns a Pandas Series.
# print(x.loc[[0,1]])
# Note: When using [], the result is a Pandas DataFrame.

'''
Named Indexes
With the index argument, you can name your own indexes.
Example:
'''
# Add a list of names to give each row a name:
# import pandas as pd
# data = {
    # "fastfoods":["burgers","pizzas","shwarmas","hotwings"],
    # "fruits":["apples","bananas","oranges","peaches"]
# }
# df = pd.DataFrame(data , index=['a','b','c','d'])
# print(df)
''' Locate Named Indexes:
 Use the named index in the loc attribute to return the specified row(s).'''
# print(df.loc['c'])

'''
Load Files Into a DataFrame
If your data sets are stored in a file, Pandas can load them into a DataFrame.
'''
# Load a comma separated file (CSV file) into a DataFrame:
# import pandas as pd 
# df = pd.read_csv("Basic/data.csv")
# print(df)

# --------DataFrames Completed-----------
