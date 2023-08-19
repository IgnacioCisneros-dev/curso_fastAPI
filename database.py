from peewee import *
import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="cartaporte"
)
cursor = db.cursor()
