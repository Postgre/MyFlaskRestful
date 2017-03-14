from flask import Flask, jsonify, abort, make_response, request, url_for


app = Flask(__name__)


task = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/')
def index():
	return 'Hello Restful'


@app.route('/todo/api/v1.0/task', methods=['GET'])
def get_task():
	return jsonify({'task': task})


@app.route('/todo/api/v1.0/task', methods=['POST'])
def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	new_task = {
		'id': task[-1]['id'] +1,
		'title': request.json['title'],
		'description': request.json.get('descrition', ''),
		'done': False
	}
	task.append(new_task)
	return jsonify({'task': task}), 201


@app.route('/todo/api/v1.0/task/<int:task_id>', methods=['GET'])
def get_certain_task(task_id):
	certain_task = filter(lambda t: t['id'] == task_id, task)
	if not certain_task:
		abort(404)
	return jsonify({'certain_task': certain_task})


@app.route('/todo/api/v1.0/task/<int:task_id>', methods=['PUT'])
def update_certain_task(task_id):
	certain_task = filter(lambda t: t['id'] == task_id, task)[0]

	if not certain_task:
		abort(404)

	if not request.json:
		abort(400)

	if 'title' in request.json:
		if type(request.json['title']) != unicode:
			abort(400)
		else:
			certain_task['title'] = request.json.get('title')

	if 'description' in request.json:
		if type(request.json['description']) is not unicode:
			abort(400)
		else:
			certain_task['description'] = request.json.get('description')

	if 'done' in request.json:
		if type(request.json['done']) is not bool:
			abort(400)
		else:
			certain_task['done'] = request.json.get('done')

	return jsonify({'certain_task': certain_task})


@app.route('/todo/api/v1.0/task/<int:task_id>', methods=['DELETE'])
def delete_certain_task(task_id):
	certain_task = filter(lambda t: t['id'] == task_id, task)
	if not certain_task:
		abort(404)
	task.remove(certain_task)

	return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
