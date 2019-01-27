@app.route("/index", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        message1 = request.form['title'];

    print ('message1')
    msg = Message('Hello', sender = 'Id@gmail.com', recipients = ['Id@gmail.com'])
    msg.body = message1
    mail.send(msg)
    return render_template("index.html")

    if __name__ == '__main__':
       app.run()