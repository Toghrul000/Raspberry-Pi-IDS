import json
from flask import Flask, jsonify, make_response, render_template, request
import datetime

app = Flask(__name__)

data = {'temperature': [0], 'humidity': [0], 'timestamp': [0], 'eventsT': ["No event yet"], 'eventsH': ["No event yet"]}

@app.route('/data', methods=['POST'])
def post_data():
    global data
    new_data = request.json
    data['temperature'].append(new_data['temperature'])
    data['humidity'].append(new_data['humidity'])
    data['timestamp'].append(new_data['timestamp'])
    return jsonify(success=True)


@app.route('/eventT', methods=['POST'])
def eventT_data():
    global data
    new_data = request.json
    data['eventsT'].append(new_data['eventT'])
    return jsonify(success=True)

@app.route('/eventH', methods=['POST'])
def eventH_data():
    global data
    new_data = request.json
    data['eventsH'].append(new_data['eventH'])
    return jsonify(success=True)

# @app.route('/data', methods=['GET'])
# def get_data():
#     global data
#     return jsonify(temperature=data['temperature'], humidity=data['humidity'], timestamp=data['timestamp'])

@app.route('/data', methods=['GET'])
def get_data():
    global data

    dataR = [data['timestamp'][-1], data['temperature'][-1], data['humidity'][-1], data['eventsT'][-1], data['eventsH'][-1]]

    response = make_response(json.dumps(dataR))

    response.content_type = 'application/json'

    # print(data['eventsT'][-1])
    # print(data['eventsH'][-1])

    return response



@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
