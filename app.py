from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('new_user')
def handle_new_user(data):
    username = data['username']
    color = data['color']
    emit('message', {'username': 'Server', 'color': '#000', 'message': f'User {username} has joined the chat.'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    emit('message', {'username': username, 'color': '#000', 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
