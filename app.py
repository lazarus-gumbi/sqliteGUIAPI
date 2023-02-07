from operator import itemgetter
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


@app.route("/api/sqlitegui", methods=["POST"])
def sqlitegui():

    content = request.get_json()
    db_name = content["db_name"]
    tables = content["tables"]
    
    try:
        conn = sqlite3.connect(f"./{db_name}.db")
        
        

        for table in tables:
            table_name = table['tablename']
            res = {}
            
            
            # [print(col) for col in table['columns']]
            [res.update(x) for x in table['columns']]
            
            columns = "(id integer PRIMARY KEY," + ",\n".join(["{} {}".format(k,v) for k,v in res.items()]) + ")"
            with sqlite3.connect(f"./{db_name}.db") as connection:
                cursor = connection.cursor()
                sql = f"CREATE TABLE {table_name}\n{columns}"
                cursor.execute(sql)

    except Exception as e:
        print(f"Error in creating database: {e}")
    finally:
        if conn:
            conn.close()

    return jsonify({"response": "200"})


if __name__ == "__main__":
    app.run(debug=True)
