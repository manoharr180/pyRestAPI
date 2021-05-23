from .dbconnection import DBConnection
import pandas as pd


def fetch_many_records(query, params=None):
    db = None
    con = None
    try:
        db = DBConnection()
        con = db.open_conn()
        cursor = con.cursor()

        if params:
            sql_query = pd.read_sql_query(query, con)
            df = pd.DataFrame(sql_query)
            result = df.reset_index().to_json(orient='records')
        else:
            sql_query = pd.read_sql_query(query, con)
            df = pd.DataFrame(sql_query)
            result = df.reset_index().to_json(orient='records')
            return result
    except ConnectionError:
        print('Something went wrong')
    finally:
        cursor.close()
        db.discon_from_db()


def fetch_one_record(query, params=None, headers=[]):
    db = None
    con = None
    try:
        db = DBConnection()
        con = db.open_conn()
        cursor = con.cursor()

        if params:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result
        else:
            # sql_query = pd.read_sql_query(query, con)
            # df = pd.DataFrame(sql_query)
            # result = df.reset_index().to_json(orient='records')
            cursor.execute(query)
            result = cursor.fetchone()
            res_obj = {}
            res_obj_list = []
            for i in range(len(headers)):
                res_obj.update({headers[i]: result[i]})
            return res_obj
    except ConnectionError:
        print('Something went wrong')
    finally:
        cursor.close()
        db.discon_from_db()


def insert_many_record(query, params=None):
    db = None
    con = None
    try:
        db = DBConnection()
        con = db.open_conn()
        cursor = con.cursor()

        if params:
            cursor.executemany(query, params)
            con.commit()
            return True
        else:
            cursor.execute(query)
            con.commit()
            return True
    except ConnectionError:
        print('Something went wrong')
    finally:
        cursor.close()
        db.discon_from_db()


def insert_one_record(query, params=None):
    db = None
    con = None
    try:
        db = DBConnection()
        con = db.open_conn()
        cursor = con.cursor()

        if params:
            cursor.execute(query, params)
            con.commit()
            return True
        else:
            cursor.execute(query)
            con.commit()
            return True
    except ConnectionError:
        print('Something went wrong')
    finally:
        cursor.close()
        db.discon_from_db()