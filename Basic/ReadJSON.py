# -----------Read Json in Pandas---------

'''
Big data sets are often stored, or extracted as JSON.
JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
In will be using a JSON file called 'data.json'. as an example 
'''
# Load the JSON file into a DataFrame:
# import pandas as pd 
# df  = pd.read_json("Basic/data.json")
# print(df.to_string())
# Tip: use to_string() to print the entire DataFrame.

'''
Dictionary as JSON:
JSON = Python Dictionary
JSON objects have the same format as Python dictionaries.
If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:
'''
import pandas as pd 
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace'],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'HR', 'Marketing', 'IT'],
    'Salary': [70000, 52000, 85000, 61000, 54000, None, 92000],
    'Age': [28, 34, 45, 29, 31, 38, 41],
    'Join_Date': ['2021-03-15', '2019-07-22', '2015-11-01', '2022-01-10', '2020-05-18', '2018-09-05', '2017-04-12']
}

# df  = pd.DataFrame(data)
# print(df)

# -----------Reading a Json file in pandas Completed---------
