import mariadb
from decimal import Decimal

#create db connection
db = mariadb.connect(
    host='localhost',
    user='pysql_user',
    password='nA*s098gE',
    database='pysql_db'
)

#query prefix-commands list
query_prefix_commands = ('select', 'show', 'describe', 'use')
#manipulation prefix-commands list
manipulate_prefix_commands = ('alter', 'insert', 'create', 'update', 'delete', 'drop')

#this function checks the prefix of the entered statement against the 'Read'/'write lists.
def query_check(sql: str) -> str:
    parts = sql.lstrip().split()
    if not parts:
        return "Unknown ..."
    prefix = parts[0].lower()
    if prefix in query_prefix_commands:
        return 'Read'
    elif prefix in manipulate_prefix_commands:
        return 'Write'
    else:
        return "Unkown ..."

def get_data(sql: str) ->str:
    #initialize DB
    cursor = db.cursor()
    action = query_check(sql)

    try:
        cursor.execute(sql)#runs user's sql statement entered into the entry() widget
        if action == 'Read':
            rows=cursor.fetchall()
            return '\n'.join(str(tuple(float(val) if isinstance(val, Decimal) else val for val in row)) for row in rows) or "No data returned."
        elif action == 'Write':
            db.commit()
            return "Query executed successfully!"
        else:
            return "Command prefix not recognized."
    except Exception as e:
        return f"Error: {e}"

def close_db_conn():
    db.close()