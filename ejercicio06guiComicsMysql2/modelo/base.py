import mysql.connector
from modelo import queries

def conectar():
    bd = mysql.connector.connect(
        host="localhost",
        user="root",
        database="bd_comics"
    )
    return bd

def query_insert_comic(comic):
    sql = queries.SQL_INSERT_COMIC
    bd = conectar()
    cursor = bd.cursor()
    valores = (comic.titulo, comic.autor, comic.editorial, comic.paginas, comic.genero)
    cursor.execute(sql, valores)
    bd.commit()
    bd.disconnect()
    
def query_select_comics():
    sql = queries.SQL_SELECT_COMICS
    bd = conectar()
    cursor = bd.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    bd.disconnect()
    return resultado

def query_delete_comic(fila):
    sql = queries.SQL_DELETE_COMIC
    bd = conectar()
    cursor = bd.cursor()
    valor = (fila,)
    cursor.execute(sql, valor)
    bd.commit()
    bd.disconnect()
 
def query_update_comic(columna, valor, id_fila):
    sql = queries.SQL_UPDATE_COMIC
    sqlf = sql.format(columna)
    bd = conectar()
    cursor = bd.cursor()
    valores = (valor, id_fila)
    cursor.execute(sqlf, valores)
    bd.commit()
    bd.disconnect()
