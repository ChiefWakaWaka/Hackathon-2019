import praw,re

def get():
    insert,dataDict,i,t = [],{},0,0
    with open("localtext.txt","r") as fp:
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
        print(key,newData)
    
def store(question,name,upvotes,answerstat,answers):
    with open("localtext.txt","a") as fp:
        enter = upvotes+"."+question+"."+name+"."+answerstat+"."
        for item in answers:
            enter = enter + item+"."
        enter = enter[0:(len(enter)-1)] + "\n"
        fp.write(enter)

    
    

old = get()
while True:
    if old != get():
        print(get())
        break
        
    

