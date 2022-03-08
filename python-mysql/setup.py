import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'playground' #The database name

TABLES = {}

#Tables definition
TABLES['memo'] = (
    "CREATE TABLE IF NOT EXISTS`memo` ("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`text` VARCHAR(400) NOT NULL,"
    "`createdAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB DEFAULT CHARSET=utf8"
)

#Database creation function
def create_db():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))

#Table creation function
def create_tables():
    cursor.execute(f"USE {DB_NAME}") #Select the DB to use

    #Loop through the tables dictionary and create the tables
    for table_name in TABLES:
        table_description = TABLES[table_name] #put the SQL queries into this variable while looping
        try:
            print(f"Creating table {table_name}", end="") #print while it is creating
            cursor.execute(table_description) #query the sql statement
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f"Table {table_name} already exists")
            else:
                print(err.msg)


create_db()
create_tables()