param = ' '.join(args)
path = userPath(param)

if len(args):
    if fs.exists(path) and fs.type(path)=="directory":
        l = "-:"+param+":-"
        for i in fs.listdir(path):
            if param=="/": param=""
            if fs.type(userPath(param+"/"+i))=="directory":
                l+="\n["+i+"]"
            else:
                l+="\n"+i
        x = l
    else:
        x = "No such directory!"
else:
    path = users[userdata["name"]]["dir"]
    l = "-:"+path+":-"
    for i in fs.listdir(path):
        if path=="/": path = ""
        if fs.type(userPath(path+"/"+i))=="directory":
            l+="\n["+i+"]"
        else:
            l+="\n"+i
    x = l


sendmsg(x)