import db_helper

def main():
    db_helper.create_table()
    db_helper.data_entry()
    db_helper.printData()
    db_helper.closeCursor()

if __name__ == '__main__':
    main()