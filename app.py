from flask import Flask, request, make_response

app = Flask(__name__)
todoDict = {}


@app.route("/todo/set/", methods=["POST"])
def recover_data():
    todoTask = request.form['todoInput']
    todoHeader = request.form['todoHeader']
    if todoHeader in todoDict.keys():
        todoDict[todoHeader].append(todoTask)
    else:
        todoDict[todoHeader] = [todoTask]
    return make_response(todoDict)


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return make_response(todoDict)


@app.route("/todo/delete/", methods=["DELETE"])
def delete_todo():

    if deleteHeader(todoDict, request.form['taskToDelete'],
                    request.form['todoHeader']):
        return make_response(todoDict, 204)
    return make_response(todoDict, 404)


def deleteHeader(dict_, taskToDelete, todoHeader):
    if taskToDelete in dict_[todoHeader]:
        dict_[todoHeader].remove(taskToDelete)
        return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
