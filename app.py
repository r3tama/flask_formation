from flask import Flask, url_for, render_template, request, Response, redirect, make_response, jsonify

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
        todoList = todoDict[todoHeader]    # if todoHeader exists, save all the data that his value contains
        todoList.append(todoTask)          # Then add the new data to the value
    else:
        todoList.append(todoTask)          # if the header doesnt exist create it and set the value
        todoDict[todoHeader] = todoList
    
    todoList = []  #Clean the array so there is no trash data when accesing each iteration
    return render_template("todo.html", data=todoDict)


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return render_template("allTodos.html", data=todoDict)

#Delete function

@app.route("/todo/delete/<string:todoDelete>", methods=["DELETE", "GET"])
def delete_todo(todoDelete):
    if deleteHeader(todoDict, todoDelete):
        return Response("Element Deleted", 204)
    return Response("Element not found", 404)


def deleteHeader(dict_, header):
    if header in dict_.keys():
        dict_.pop(header)
        return True
    return False



if __name__ == '__main__':
    app.run(debug=True)
