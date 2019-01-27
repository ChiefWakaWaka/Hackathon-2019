

def store(upvotes,question,name,answerstat,answers):
    with open("localtext.txt","a") as fp:
        enter = upvotes+"."+question+"."+name+"."+answerstat+"."
        answers = answers.split(",")
        for item in answers:
            enter = enter + item+"."
        enter = enter[0:(len(enter)-1)] + "\n"
        fp.write(enter)


while True:
    store(input(":"),input(":"),input(":"),input(":"),input(":"))
    import sampleCSVAccess.py 
    #print(csvget.pull())
