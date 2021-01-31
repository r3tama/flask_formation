
from flask import Flask, url_for, render_template, request, Response, redirect

app = Flask(__name__)

todoDict = {

}

todoList = []


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/todoshow/", methods=['GET'])
def show_todo_form():
    return render_template("todo.html")


@app.route("/todo/set/", methods=['POST'])
def recover_data():
    global todoList
    todoTask = request.form['todoInput']
    todoHeader = request.form['todoHeader'] 

    if todoHeader in todoDict.keys():
        todoList = todoDict[todoHeader] 
        todoList.append(todoTask)
    else: 
        todoList.append(todoTask)
        todoDict[todoHeader] = todoList
    
    todoList = []
    return render_template("todo.html", data=todoDict) 


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return render_template("allTodos.html", data=todoDict)

"""
@app.route("/todo/show/<int:todo_id>/")
def show_one_todo(todo_id=None):
    return "The id is {}".format(todo_id)
"""


def checkIfEmpty(inputString):
    return len(inputString) <= 0


def checkHeader(dict_, header):
    return header in dict_.keys()


if __name__ == '__main__':
    app.run(debug=True)
