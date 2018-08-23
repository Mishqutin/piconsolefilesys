param = ' '.join(args)
path = userPath(param)
print(path)
if len(args):
    if fs.exists(path) and fs.type(path)=="directory":
        l = ""
        for i in fs.listdir(path):
            if fs.type(userPath(param+"/"+i))=="directory":
                l+="\n["+i+"]"
            else:
                l+="\n"+i
        x = l
    else:
        x = "No such directory!"
else:
    path = users[userdata["name"]]["dir"]
    l = ""
    for i in fs.listdir(path):
        if fs.type(userPath(param+"/"+i))=="directory":
            l+="\n["+i+"]"
        else:
            l+="\n"+i
    x = l


sendmsg(x)