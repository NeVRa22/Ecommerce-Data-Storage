import mysql.connector
import random
import time
import datetime


# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("mySQL Database connection successful")
    except Exception as err:
        print(f"Error:'{err}'")

    return connection

    # Implement the logic to create the server connection


# This method will create the database and make it an active database
def create_and_switch_database(connection, db_name, switch_db):
    cursor = connection.cursor()
    try:
        drop_query = 'DROP DATABASE IF EXISTS ' + db_name
        db_query = 'CREATE DATABASE ' + db_name
        switch_query = 'USE ' + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print("Database created successfully")
    except Exception as err:
        print(f"Error in creating database:'{err}")

    # For database creatio nuse this method
    # If you have created your databse using UI, no need to implement anything


# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error in creating connection with database: '{err}'")
    return connection


# Use this function to create the tables in a database
def create_table(connection, table_creation_statement):
    cursor = connection.cursor()
    try:
        cursor.execute(table_creation_statement)
        connection.commit()
        print("Table creation successful")
    except Exception as err:
        print(f"Error in Table creation : '{err}'")


# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error in insert query: '{err}'")
    # This method will perform creation of the table
    # this can also be used to perform single data point insertion in the desired table


# retrieving the data from the table based on the given query
def select_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f"Error in insert query: '{err}'")

    # fetching the data points from the table 


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error in insert many records: '{err}")
