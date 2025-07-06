from db.practice_db import close_db_conn
from gui.dashboard import sql_statement

def main() ->None:
    sql_statement()
    close_db_conn()

if __name__ == '__main__':
    main()