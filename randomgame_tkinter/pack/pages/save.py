import sqlite3

def save_data(username,level, time, generate_number, count):
    connection = sqlite3.connect("./database.sqlite")
    cur = connection.cursor()

    query = """INSERT INTO score(username,level, times, generate_number, count) values (?, ?, ?, ?, ?)"""
    cur.execute(query, [username, level, time, generate_number, count])
    connection.commit()
    connection.close()