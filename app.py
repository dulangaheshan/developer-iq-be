from flask import Flask
from flask import request

from utils.dynamodb_handler import get_repositories, get_all_repositories, get_contributors_in_repository, \
    get_events_by_key

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/all_repositories')
def all_repositories():
    return get_all_repositories()


@app.route('/api/repositories', methods=['GET'])
def all_repositories_for_day_id():
    day_id = request.args.get('day_id')
    return get_repositories(day_id)


@app.route('/api/contributors', methods=['GET'])
def get_contributors_in_repo():
    repo = request.args.get('repo')
    return get_contributors_in_repository(repo)


@app.route('/api/events',  methods=['GET'])
def get_events():
    repo = request.args.get('repo')
    day_id = request.args.get('day_id')
    return get_events_by_key(repo, day_id)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
