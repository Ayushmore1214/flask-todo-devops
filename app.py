from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return "Welcome to the Flask To-Do App!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        tasks.append({'task': task})
        return jsonify({'message': 'Task added!'}), 201
    return jsonify({'error': 'Task is required'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
