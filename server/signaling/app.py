from flask import Flask
from flask import request
from flask import jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def index():
    return 'Intelligent Open Network'

@app.route("/checkIp", methods=["GET"])
def on_check_ip():
    return jsonify({'ip': request.remote_addr}), 200

@socketio.on('push', namespace='/nodes')
def on_push(data):
    emit('update', { 'data': data }, broadcast=True)

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(
        app, host='0.0.0.0', port=5000, use_reloader=False, debug=True, log_output=True
    )