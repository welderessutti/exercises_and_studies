import mysql.connector
import json
from datetime import date


def create_db_connection(user, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user=f"{user}",
        password=f"{password}",
        database="brasileirao"
    )
    return mydb


def create_cursor(mydb):
    mycursor = mydb.cursor()
    return mycursor


def create_db_exists(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")


def create_table_exists(cursor, table_name):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` "
                   f"(pos varchar(20), "
                   f"nm_time varchar(50), "
                   f"pg smallint, "
                   f"j smallint, "
                   f"v smallint, "
                   f"e smallint, "
                   f"d smallint, "
                   f"gp smallint, "
                   f"gc smallint, "
                   f"sg smallint, "
                   f"ap smallint)"
                   f"DEFAULT CHARSET = utf8")


def open_json_file(file_name):
    with open(f"../web_scraping/{file_name}.json", "r", encoding="utf-8") as file:
        brasileirao = json.load(file)
        file.close()
    return brasileirao


def insert_into(cursor, table_name, json_file):
    statement = f"INSERT INTO `{table_name}` (pos, nm_time, pg, j, v, e, d, gp, gc, sg, ap) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for team_row in json_file["brasileirao"]:
        data = (team_row['POS'], team_row['TIME'], team_row['PG'], team_row['J'], team_row['V'], team_row['E'], team_row['D'], team_row['GP'], team_row['GC'], team_row['SG'], team_row['%'])
        cursor.execute(statement, data)


table_name = f"classificacao_{date.today()}"
file_name = f"classificacao_{date.today()}"

connection = create_db_connection("root", "******")
cursor = create_cursor(connection)

create_db_exists(cursor, "brasileirao")
create_table_exists(cursor, table_name)

file = open_json_file(file_name)
insert_into(cursor, table_name, file)

connection.commit()
cursor.close()
