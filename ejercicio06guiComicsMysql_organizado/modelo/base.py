import mysql.connector
from modelo import queries, clases

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
    valores = (comic.titulo, comic.autor, comic.editorial, comic.paginas, comic.genero, comic.tapa, comic.coleccion)
    cursor.execute(sql, valores)
    bd.commit()
    id_generado = cursor.lastrowid
    bd.disconnect()
    return id_generado
    
def query_select_comics():
    sql = queries.SQL_SELECT_COMICS
    bd = conectar()
    cursor = bd.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    bd.disconnect()
    return resultado

def query_select_comic(id):
    sql = queries.SQL_SELECT_COMIC
    bd = conectar()
    cursor = bd.cursor()
    valor = (id,)
    cursor.execute(sql, valor)
    comic_seleccion = cursor.fetchone()
    bd.disconnect()
    objeto_comic = clases.Comic(id = comic_seleccion[0], titulo = comic_seleccion[1], autor = comic_seleccion[2], \
        editorial = comic_seleccion[3], genero = comic_seleccion[5], \
        paginas = comic_seleccion[4], tapa = comic_seleccion[6], coleccion = comic_seleccion[7])
    return objeto_comic

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

def query_update_comic_ver(comic):
    sql = queries.SQL_UPDATE_COMIC_VER
    bd = conectar()
    cursor = bd.cursor()
    valores = (comic.titulo, comic.autor, comic.editorial, comic.genero, comic.tapa, comic.paginas, comic.coleccion, comic.id)
    cursor.execute(sql, valores)
    bd.commit()
    bd.disconnect()
    