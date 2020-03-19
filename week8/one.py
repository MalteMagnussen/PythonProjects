import pymysql

# FRAIL RELIGION
# OPGAVE ET
# Hent følgende data:
# 1. Navn på de personer som har en salary der er højere end 50.000
# 2. Navn på dem som har efternavnet "Juhlborg"
# 1. SELECT `firstname`, `lastname` FROM pythonexercise.pythondemo WHERE `salary`>50000;
# 2. SELECT `firstname`, `lastname` FROM pythonexercise.pythondemo WHERE lastname='Juhlborg';


def getNames(statement):

    connection = pymysql.connect(
        user='root', password='root', host='127.0.0.1', port=3306, db='pythonexercise')

    with connection.cursor() as cursor:

        query = (statement)

        cursor.execute(query)

        for(firstname, lastname) in cursor:
            print("First Name:", firstname)
            print("Last Name:", lastname)
            print("")

        print("What we sent to MySQL:", cursor._last_executed)

    connection.close()


# 1.
print("\nNavn på de personer som har en salary der er højere end 50.000\n")
getNames('SELECT firstname, lastname FROM pythonexercise.pythondemo WHERE salary>50000;')
# 2.
print("\nNavn på dem som har efternavnet 'Juhlborg'\n")
getNames('SELECT `firstname`, `lastname` FROM pythonexercise.pythondemo WHERE lastname="Juhlborg";')
