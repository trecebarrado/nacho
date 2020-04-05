SQL_INSERT_COMIC = "INSERT INTO tabla_comics (Id, titulo, autor, editorial, paginas, genero) VALUES (NULL, %s, %s, %s, %s, %s);"
SQL_SELECT_COMICS = "SELECT * FROM tabla_comics;"
SQL_DELETE_COMIC = "DELETE FROM tabla_comics WHERE Id = %s;"
SQL_UPDATE_COMIC = "UPDATE tabla_comics SET {} = %s WHERE Id = %s"