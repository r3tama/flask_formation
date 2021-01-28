
from flask import Flask, url_for, render_template, request, Response, redirect

app = Flask(__name__)


todoList = {
    "Todo": [],
}


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/todoshow/", methods=['GET'])
def show_todo_form():
    return render_template("todo.html")


@app.route("/todo/set/", methods=['POST'])
def recover_data():
    todoTask = request.form['todoInput']
    if not checkIfEmpty(todoTask):
        todoList["Todo"].append(todoTask)
        return render_template("todo.html", data=todoList)
    return render_template("todo.html", error="You need to enter a non empty todo task")


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return render_template("allTodos.html", data=todoList)

def checkIfEmpty(inputString):
    return len(inputString) <= 0


if __name__ == '__main__':
    app.run(debug=True)
