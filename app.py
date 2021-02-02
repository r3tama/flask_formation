from flask import Flask, request, make_response
from shared.utils import deleteValueFromListInDict, existsKeyInDict, swapTaskFromListInDict
app = Flask(__name__)
todoDict = {}


@app.route("/todo/set/", methods=["POST"])
def recover_data():
    if existsKeyInDict(request.form['todoHeader'], todoDict):
        todoDict[request.form['todoHeader']].append(request.form['todoInput'])
    else:
        todoDict[request.form['todoHeader']] = [request.form['todoInput']]
    return make_response(todoDict)


@app.route("/todo/showAll/", methods=['GET'])
def show_all_todos():
    return make_response(todoDict)


@app.route("/todo/delete/", methods=["DELETE"])
def delete_todo():
    if deleteValueFromListInDict(request.form["todoHeader"], request.form["taskToDelete"], todoDict):
        return make_response(todoDict, 204)
    return make_response(todoDict, 404)


@app.route("/todo/changeTask/", methods=['POST'])
def change_task():
    if swapTaskFromListInDict(request.form["todoHeader"],request.form["swapouttask"],request.form["swapintask"],todoDict):
        return make_response("True")
    return make_response("False")



if __name__ == '__main__':
    app.run(debug=True)
