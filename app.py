from flask import Flask, request, make_response, render_template, redirect
from shared.utils import deleteValueFromListInDict, existsKeyInDict, swapTaskFromListInDict
app = Flask(__name__)
todoDict = {}


@app.route("/todo/set", methods=["POST"])
def recover_data():
    if existsKeyInDict(request.form['todoHeader'], todoDict):
        todoDict[request.form['todoHeader']].append(request.form['todoInput'])
    else:
        if request.form['todoInput']:
            todoDict[request.form['todoHeader']] = [request.form['todoInput']]
    return redirect("/todo/showAll")

@app.route("/", methods=["GET"])
def base_template():
    return render_template('base_template.html')

@app.route("/fillFormRender", methods=["GET"])
def render_form():
    return render_template('form_input.html')

@app.route("/todo/showAll", methods=['GET'])
def show_all_todos():
    return render_template('show_dict.html',dict=todoDict)


@app.route("/todo/delete", methods=["POST"])
def delete_todo():
    deleteValueFromListInDict(request.form["todoHeader"], request.form["taskToDelete"], todoDict)
    return redirect("/todo/showAll")
    


@app.route("/todo/changeTask", methods=['POST'])
def change_task():
    if swapTaskFromListInDict(request.form["todoHeader"],request.form["swapouttask"],request.form["swapintask"],todoDict):
        return make_response(todoDict, 200)
    return make_response(todoDict, 404)



if __name__ == '__main__':
    app.run(debug=True)
