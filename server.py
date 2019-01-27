from flask import Flask, request, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
global processedText
global ree
ree = False
processedText = []
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    global processedText
    return render_template('session.html', question=processedText)


@app.route('/', methods=['POST'])
def post():
    global processedText
    text = request.form['text']
    processedText = [text] + processedText
    re = True
    return render_template('session.html', question=processedText)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':#
    app.run(host='10.41.0.35', port=8000)
