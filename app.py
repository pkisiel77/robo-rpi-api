import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/robo', methods=['POST'])
def robo():
    if request.method != "POST":
        return

    my_bytes_value = request.data
    my_json = my_bytes_value.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    s = json.dumps(data, indent=4, sort_keys=True)

    print(s)

    return s


if __name__ == '__main__':
    app.run()
