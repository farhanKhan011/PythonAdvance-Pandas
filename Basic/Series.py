# ------------Pandas Series----------------

'''
What is a Series?
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
'''
# Create a simple Pandas Series from a list:
# import pandas as pd 
# arr = [1,3,7]
# x = pd.Series(arr)
# print(x)
'''
Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
Example
Return the first value of the Series:
'''
# print(x[0])


'''
Create Labels
With the index argument, you can name your own labels.
'''
# Create your own labels
# import pandas as pd
# data = [2,4,8]
# x = pd.Series(data, index = ["a","b","c"])
# print(x)
# When you have created labels, you can access an item by referring to the label.
# print(x["b"])

# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
# Create a simple Pandas Series from a dictionary:
# import pandas as pd
# calories = {
#     "day1":380,
#     "day2":430,
#     "day3":380
# }
# myvar = pd.Series(calories)
# print(myvar)

'''
To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
'''
# import pandas as pd 
# letsEat = {
#     "Burger":450,
#     "Pizza":2400,
#     "Noodles":300,
#     "Shwarma":200,
# }

# myorder = pd.Series(letsEat, index = ["Burger","Shwarma"])
# print(myorder)

'''
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table.
Create a DataFrame from two Series:
'''
# import pandas as pd 
# data = {
#   "fastFood": [420, 380, 390],
#   "price": [50, 40, 45]
# }
# OrganizeData = pd.DataFrame(data)
# print(OrganizeData)

# ---------Pandas Series Completed----------
