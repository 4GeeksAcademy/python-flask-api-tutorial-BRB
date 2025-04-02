from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

todos = [
      {'label':"Walk the dog", "done": False},
      {'label': "Take out the trash", "done": False},
      {'label': "Clean the windows", "done": False},
      ]



@app.route('/todos',methods=['GET'])
def hello_world():
        json_text = jsonify(todos)
        return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body= request.json
    todos.append(request_body)
    request_body=jsonify(todos)

    return request_body







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)