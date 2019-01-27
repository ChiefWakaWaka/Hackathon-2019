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
        return render_template('index.html', question=processedT$


@app.route('/', methods=['POST'])

def post():
        global processedText
        text = request.form['text']
        processedText = [text] + processedText
        re = True
        return render_template('index.html', question=processedT$


if __name__ == '__main__':#
        app.run(host='10.0.0.135', port=80)
        if re = True:
                app.run()
                re = False
