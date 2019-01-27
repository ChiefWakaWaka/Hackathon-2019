from flask import Flask, request, render_template
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
        return render_template('index.html', question=processedText)


@app.route('/', methods=['POST'])
def post():
        global processedText
        text = request.form['text']
        processedText = [text] + processedText
        re = True
        return render_template('index.html', question=processedText)


if __name__ == '__main__':#
        app.run(host='127.0.0.1', port=8000)
        if re == True:
                app.run()
                re = False
