import praw,re
from flask import Flask, render_template, request
from flask_socketio import SocketIO
global list
lis = []
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/', methods=['GET','POST'])
def sessions():
    print('Handling root')
    return render_template('session.html')

def messageReceived(methods=['POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['POST']):
    global lis
    print('received my event: ' + str(json))
#    json = {'user_name':'a', 'message':'a'}
    #{u'message': u'a', u'user_name': u'a'}{u'message': u'a', u'user_name': u'a'}
    txt = json[u'message']
    name = json[u'user_name']
    upvote = 1
    answerstat = 0
    answers = ""
    store(upvote,txt,name,answerstat,answers)
    data = get()
    for key in data:
        array = data[key]
        json[u'up'] = key
        json[u'message'] = array[0]
        json[u'name'] = array[1]
        json[u'answerstat'] = array[2]
        #for i in range(len(array)-3):
        #    newArray[i] = array[i+3]

        json[u'answers'] = data[3:]
        socketio.emit('my response', json, callback=messageReceived)


@socketio.on('button event')
def handleMessage(id):
    upvotes[id] = upvotes[id] + 1

def get():
    insert,dataDict,i,t = [],{},0,0
    with open("/Users/Sami/Documents/Folder/Coding/Python/Hackathon-2019/localtext.txt","r") as fp:
        for row in fp:
            data = row.split(".")
            for item in data:
                if item[len(item)-1] == "\n":
                    data[t] = item[0:len(item)-1]
                t = t + 1
            t = 0
            dataDict[data[0]] = [data[1],data[2],data[3]]
            for a in range(len(data)-4):
                 dataDict[data[0]].append(data[4 + a])
            i = i + 1
    return dataDict

def pull():
    data = get()
    for key in sorted(data, reverse=True):
        newData = data[key]

def store(question,name,upvotes,answerstat,answers):
    with open("localtext.txt","a") as fp:
        enter = upvotes+"."+question+"."+name+"."+answerstat+"."
        for item in answers:
            enter = enter + item+"."
        enter = enter[0:(len(enter)-1)] + "\n"
        fp.write(enter)


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1", port='5000',debug=True)
