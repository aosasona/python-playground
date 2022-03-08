import mysql.connector

config = {
    "user" : "root",
    "password" : "jesudarasimi",
    "host" : "localhost",
    "database"  : "playground"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()