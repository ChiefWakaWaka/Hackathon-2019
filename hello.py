from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

#RUN IN TERMINAL:
#   export FLASK_APP=hello.py
#   flask run
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
