param = ' '.join(args)
path = userPath(param)
print(path)
if len(args):
    if fs.exists(path) and fs.type(path)=="directory":
        x = str(fs.listdir(path))
    else:
        x = "No such directory!"
else:
    x = str(fs.listdir(users[userdata["name"]]["dir"]))


sendmsg(x)