import psycopg2
import sys

conn = None
def connect(host, user, password, dbname):
    global conn
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=dbname
        )
        return conn
    except Exception as e:
        print(f"Exception occurred: {e}")
        sys.exit(1)


def createtable(query):
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()

def selectfromtable(tablename):
    query = f'SELECT * FROM {tablename};'
    try:
        cur = conn.cursor()
        cur.execute(query)
        traineedata = cur.fetchall()
        return traineedata
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()

def inserttrainee(id, name, age, track):
    query = f"INSERT INTO trainee (id, name, age, track_id) VALUES ({id}, '{name}', '{age}', '{track}');"
    try:
        cur = conn.cursor()
        cur.execute(query, (id, name, track))
        conn.commit()
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()

def updatetrainee(id, name, age, track):
    query = f"UPDATE trainee SET name = '{name}', track_id = '{track}', age = {age} WHERE id = {id};"
    try:
        cur = conn.cursor()
        cur.execute(query, (name, track, id))
        conn.commit()
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()

def deletetrainee(id):
    query = f"DELETE FROM trainee WHERE id = {id};"
    try:
        cur = conn.cursor()
        cur.execute(query, (id,))
        conn.commit()
    except Exception as e:
        print(f"Exception occurred: {e}")
    finally:
        cur.close()