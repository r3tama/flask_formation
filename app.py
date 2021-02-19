import redis
from flask import Flask, request, make_response, render_template, redirect
from shared.utils import deleteValueFromListInDict, existsKeyInDict, swapTaskFromListInDict, eliminateTodoList
app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)
todoDict = {}


@app.route("/todo/set", methods=["POST"])
def recover_data():
    if existsKeyInDict(request.form['todoHeader'], todoDict):
        todoDict[request.form['todoHeader']].append(request.form['todoInput'])
    else:
        if request.form['todoInput']:
            todoDict[request.form['todoHeader']] = [request.form['todoInput']]
    return redirect("/fillFormRender")

@app.route("/", methods=["GET"])
def base_template():
    return render_template('base_template.html')

@app.route("/fillFormRender", methods=["GET"])
def render_form():
    return render_template('form_input.html',dict=todoDict)



@app.route("/todo/delete", methods=["POST"])
def delete_todo():
    deleteValueFromListInDict(request.form["todoHeader"], request.form["taskToDelete"], todoDict)
    return redirect("/fillFormRender")

@app.route("/list/delete", methods=["POST"])
def delete_list():   
    eliminateTodoList(request.form["todoList"],todoDict)
    return redirect("/fillFormRender")

@app.route("/todo/changeTask", methods=['POST'])
def change_task():
    if swapTaskFromListInDict(request.form["todoHeader"],request.form["swapouttask"],request.form["swapintask"],todoDict):
        return make_response(todoDict, 200)
    return make_response(todoDict, 404)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
