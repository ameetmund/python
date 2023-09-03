import sqlite3

db = 'mydb.db'
table_name = 'employee'
conn = sqlite3.connect(db)
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name \
        + '(ID, FIRST_NAME, LAST_NAME, DEPARTMENT)'
    c.execute(sql)
    print("Table created")

def data_entry():
    sql = 'INSERT INTO ' + table_name + ' VALUES' \
        + "('200', 'Ameet', 'Mund', 'Marketing')"
    c.execute(sql)
    print("Data inserted into table")

def printData():
    sql = 'SELECT * FROM ' + table_name
    c.execute(sql)
    for row in c.fetchall():
        print('ID   ', 'FIRST_NAME    ', 'LAST_NAME    ', 'DEPARTMENT   ')
        print('---- ', '-----------   ', '----------   ', '-----------')
        print(row[0], "  ", row[1], "        ", row[2], "    ", row[3], "        ")
    print("Data selected")

def deleteTask():
    sql = 'DELETE FROM ' + table_name
    c.execute(sql)
    print("Data Deleted")

def closeCursor():
    c.close()
    conn.close()
    print("Cursor closed")