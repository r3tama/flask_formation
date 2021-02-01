from flask import Flask, request, make_response
from shared.utils import deleteValueFromDict, existsKeyInDict
app = Flask(__name__)
todoDict = {}


@app.route("/todo/set/", methods=["POST"])
def recover_data():
    todoTask = request.form['todoInput']
    todoHeader = request.form['todoHeader']
    if existsKeyInDict(todoHeader, todoDict):
        todoDict[todoHeader].append(todoTask)
    else:
        todoDict[todoHeader] = [todoTask]
    return make_response(todoDict)


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return make_response(todoDict)


@app.route("/todo/delete/", methods=["DELETE"])
def delete_todo():
    if deleteValueFromDict(request.form["todoHeader"], request.form["taskToDelete"], todoDict):
        return make_response(todoDict, 204)
    return make_response(todoDict, 404)


if __name__ == '__main__':
    app.run(debug=True)
