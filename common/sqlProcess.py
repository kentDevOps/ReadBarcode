import sqlite3
import os,sys

def get_sys_path_sql(strDbName):
    strAbsPath = os.path.abspath(sys.argv[0])
    strDirPath = os.path.dirname(strAbsPath)
    strDbPath = os.path.join(strDirPath,"database") + f"\\{strDbName}"
    return strDbPath
def creat_sql_conn():
    db_path = get_sys_path_sql("label_approval.db")
    cnn = sqlite3.connect(db_path)
    cursor = cnn.cursor()
    return cnn, cursor
def get_value_db(tabelName,colName):
    cnn, cursor = creat_sql_conn()
    query = f"SELECT {colName} FROM {tabelName}"
    cursor.execute(query)
    result = cursor.fetchall()
    cnn.close()
    return result
def get_value_cbx_line(tabelName,colName,conditionCol,conditionVal):
    cnn, cursor = creat_sql_conn()
    query = f"SELECT {colName} FROM {tabelName} WHERE {conditionCol} = ?"
    cursor.execute(query, (conditionVal,))
    result = cursor.fetchall()
    cnn.close()
    return result