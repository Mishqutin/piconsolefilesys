import posixpath as osp
import html

def txtToHtml(string):
    x = html.escape(string).replace("\n", "<br>")
    return x

SaveFsDisconnect = 1
users = {}

def onClientConnect(userdata):
    global users
    f = open(CWD+"/users", 'r')
    users = eval(f.read())
    f.close()
    
    if not userdata["name"] in users:
        users[userdata["name"]] = {"dir": "/"}
    

server.onClientConnect = onClientConnect

def onClientDisconnect(userdata):
    global users
    f = open(CWD+"/users", 'w')
    f.write(str(users))
    f.close()
    
    if SaveFsDisconnect:
        f = open(CWD+"/FILESYSTEM", 'w')
        f.write(str(fs.filesystem))
        f.close()
    

server.onClientDisconnect = onClientDisconnect


def sendmsg(string, escHtml=1):
    if escHtml:
        c.send( txtToHtml(string).encode() )
    else:
        c.send( string.encode() )



def userPathShit(path):
    if path[0]=="/":
        return path
    else:
        return users[userdata["names"]]["dir"]+"/"+path

def userPath(path):
    userpath = users[userdata["name"]]["dir"]
    if not len(path): return userpath
    if path=="..":
        x = osp.normpath(userpath + "/" + path)
    elif path[0]=="/":
        x = osp.normpath(path)
    else:
        if userpath=="/":
            x = osp.normpath(userpath + path)
        else:
            x = osp.normpath(userpath + "/" + path)
    return x