import pandas as pd

# Task: Get the data on people on the Titanic, their class, sex age, ticket price and whether they survived.
# Answer: I manually downloaded the .zip file and extracted the files.

# Task: Load into pandas dataframe.
# Answer:
df = pd.read_csv("train.csv")
print("read_csv")
print(df)

# Task: Drop the PassengerId, Name, Ticket, Cabin columns from the dataframe
# Answer:
# inplace=true er at den ændrer df, i stedet for at oprette en ny og så returnere den
df.drop(["PassengerId", "Name", "Ticket", "Cabin"], "columns", inplace=True)
print()
print(".drop inplace=true")
print(df)
