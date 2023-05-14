INSERT_LIST = "INSERT INTO list (todo, creation_date) VALUES(%s, %s) RETURNING id;"
SELECT_LIST = "SELECT id, todo, creation_date FROM list;"
PUT_LIST = "UPDATE list SET todo = %s WHERE id = %s;"
DELETE_LIST = "DELETE FROM list WHERE id = %s;"