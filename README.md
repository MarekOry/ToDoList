This is a simple "to do" list management app in Python.

In order to install all required libraries type in the console while inproject directory: pip install -r requirements.txt

Before running an application make sure to create a database with table called "list" and define adress in ".env" file.

The "list" table need 3 columns: id(int), todo(varchar), creation_date(date). id column must be an autoincrement primary key.

After that app can be started by typing "flask run" in a console.

I use Postman to send requests in JSON.

Endpoints are defined under paths:

http://127.0.0.1:5000/api/get/todo - get request shows all data from list table

http://127.0.0.1:5000/api/post/todo - post request adds new todo to a list, only todo value needs to be defined in request. ex. {"todo": "buy milk"}

http://127.0.0.1:5000/api/put/todo - put request changes a todo. Request needs id number that you want to change and new todo value. ex.{"id": "1", "todo": "buy juice"}

http://127.0.0.1:5000/api/delete/todo - delete request removes a record from a list. id needs to be defined in a request. ex. {"id": "1"}
