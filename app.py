from flask import Flask, url_for, render_template, request, Response, redirect
app = Flask(__name__)
todoDict = {}

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/todoshow/", methods=['GET'])
def show_todo_form():
    return render_template("todo.html")


@app.route("/todo/set/", methods=['POST'])
def recover_data():
    todoArray = []
    todoTask = request.form['todoInput']
    todoHeader = request.form['todoHeader']
    if todoHeader in todoDict.keys():
        todoDict[todoHeader].append(todoTask)
    else:
        todoArray.append(todoTask)
        todoDict[todoHeader] = todoArray
    return render_template("todo.html", data=todoDict)


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return render_template("allTodos.html", data=todoDict)


def checkIfEmpty(inputString):
    return len(inputString) <= 0


def checkHeader(dict_, header):
    return header in dict_.keys()


if __name__ == '__main__':
    app.run(debug=True)
