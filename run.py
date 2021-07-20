from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)

messages = [{'username': 'Admin', 'text':'Hola, Bienvenido'}]

@app.route('/<username>/')
def chat(username):
    return render_template('chat.html', username = username)

# Evento de conexión
@socketio.on('connect')
def connect(data):
    join_room('chat_room')
    emit('messages', messages, to='chat_room')

# Evento que recibe los mensajes
@socketio.on('chat_messages')
def message(data):
    messages.append(data)
    emit('messages', messages, to='chat_room')


if __name__ == '__main__':
    socketio.run(app)