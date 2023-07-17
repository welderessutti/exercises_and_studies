import mysql.connector
import json
from datetime import date


def create_db_connection(user_, password_):
    mydb = mysql.connector.connect(
        host="localhost",
        user=f"{user_}",
        password=f"{password_}",
    )
    return mydb


def create_cursor(connection_):
    mycursor = connection_.cursor()
    return mycursor


def create_db_exists(cursor_, db_name_):
    cursor_.execute(f"CREATE DATABASE IF NOT EXISTS {db_name_}")


def create_table_exists(cursor_, db_name_, table_name_):
    cursor_.execute(f"USE {db_name_}")
    cursor_.execute(f"CREATE TABLE IF NOT EXISTS `{table_name_}`"
                    f"(pos varchar(20),"
                    f"nm_time varchar(50),"
                    f"pg smallint,"
                    f"j smallint,"
                    f"v smallint,"
                    f"e smallint,"
                    f"d smallint,"
                    f"gp smallint,"
                    f"gc smallint,"
                    f"sg smallint,"
                    f"ap smallint)"
                    f"DEFAULT CHARSET = utf8")


def open_json_file(file_name_):
    with open(f"../web_scraping/{file_name_}.json", "r", encoding="utf-8") as file_:
        brasileirao = json.load(file_)
        file_.close()
    return brasileirao


def insert_into(cursor_, db_name_, table_name_, json_file_):
    statement = f"INSERT INTO `{table_name_}` (pos, nm_time, pg, j, v, e, d, gp, gc, sg, ap)" \
                f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor_.execute(f"USE {db_name_}")

    for team in json_file_["brasileirao"]:
        data = (team["POS"],
                team["TIME"],
                team["PG"],
                team["J"],
                team["V"],
                team["E"],
                team["D"],
                team["GP"],
                team["GC"],
                team["SG"],
                team["%"])

        cursor_.execute(statement, data)


user = "root"
password = "Luvmadoggos#1"
db_name = "brasileirao"
table_name = f"classificacao_{date.today()}"
file_name = f"classificacao_{date.today()}"

connection = create_db_connection(user, password)
cursor = create_cursor(connection)

create_db_exists(cursor, db_name)
create_table_exists(cursor, db_name, table_name)

file = open_json_file(file_name)
insert_into(cursor, db_name, table_name, file)

connection.commit()
cursor.close()
connection.close()
