from flask import Flask
from flask import request

# from utils.dynamodb_handler import get_repositories, get_all_repositories, get_contributors_in_repository

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.route('/all_repositories')
# def all_repositories():
#     return get_all_repositories()


# @app.route('/repositories', methods=['GET'])
# def all_repositories_for_day_id():
#     day_id = request.args.get('day_id')
#     return get_repositories(day_id)


# @app.route('/contributors', methods=['GET'])
# def get_contributors_in_repo():
#     repo = request.args.get('repo')
#     return get_contributors_in_repository(repo)


# @app.route('/events')
# def get_events():  # put application's code here
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
