import pandas as pd
import pymysql
from sqlalchemy import create_engine
# FRAIL RELIGION
# OPGAVE TO
# Anvend filen befkbhalderstatkode.csv
data = pd.read_csv("befkbhalderstatkode.csv")
# Lav denne fil om til en mysql table med navnet statskode
name = "statskode"
print("DATA:\n", data)
# Connection Info
username = "root"
password = "root"
ip = "localhost"
port = "3306"
database = "pythonexercisetwo"
# Connection String
connection_string = 'mysql+pymysql://' + username + ':' + password + \
    '@' + ip + ':'+port+'/'+database + '?charset=utf8mb4'
print(connection_string)
# Make connection
engine = create_engine(connection_string)
# Connect to the database
connection = pymysql.connect(
    host=ip, user=username, password=password, db=database)
# Execute the to_sql for writting DF into SQL
data.to_sql(name, engine, if_exists='replace', index=False)
# Now we have the data in the database...
# So lets see if all worked by printing the data in database.
# Make query
sql_query = f'SELECT * FROM {name}'
# create cursor
with connection.cursor() as cursor:
    # Execute query
    cursor.execute(sql_query)
    # Fetch all the rows
    for i in cursor.fetchall():
        print(i)
