import socket
import os, sys, time

DEBUG = 0

CWD = os.getcwd()

f = open("config.txt", 'r')
config = eval(f.read())
f.close()

IP = config["IP"]

f = open("text.txt", 'r')
text = eval(f.read())
f.close()

# Server functions
def uploadFile(name, data):
    c.send( ( "#//download " + name ).encode() )
    c.recv(8)
    c.send(data)

# DO NOT USE VVV
def downloadFileFull():
    c.send(b"ok")
    
    code = b""
    while True:
        data = c.recv(1048576) # 1MB
        if not len(data): break
        code += data
    return code

# Use this vv
def downloadFile():
    code = b""
    c.setblocking(0)
    sTime = time.time()
    while True:
        try:
            data = c.recv(1048576) # 1MB
        except:
            data = b""
        if not len(data) and time.time()-sTime>1:
            break
        elif len(data):
            sTime=time.time()
        code += data
    c.setblocking(1)
    return code

def refuseConnection():
    global REFUSE_CONNECTION
    REFUSE_CONNECTION = 1

# 
class server:
    def onClientConnect(userdata):
        pass
    
    def onClientEntryCodePass(userdata):
        pass
    
    def onClientEntryCodeFail(userdata):
        pass
    
    def onCommandStartExecute(userdata, cmd, args):
        pass
    
    def onCommandExecute(userdata, cmd, args):
        pass
    
    def onCommandExecuteFail(userdata, cmd, args):
        pass

    def onClientDisconnect(userdata):
        pass



# Chceck if dir exists, isn't empty and config allows loading libs
if os.path.isdir(CWD+"/libs") and len(os.listdir(CWD+"/libs")) and config["loadLibs"]:
    config["loadLibs"] = True
else:
    config["loadLibs"] = False

# Load libraries 
if config["loadLibs"]:
    print("Loading libraries")
    for i in os.listdir(CWD+"/libs"):
        if i[-3:]==".py":
            print(i)
            f = open(CWD+"/libs/"+i, 'r')
            code = f.read()
            f.close()
            exec(code, globals())


s = socket.socket()
s.bind(IP)
s.listen(1)
if DEBUG: print("DEBUG mode on")
print("Running")
while True:
    REFUSE_CONNECTION = 0
    c, addr = s.accept()
    
    rawUserData = (c.recv(2048)).decode("ASCII")
    sepIndex = rawUserData.find("@")
    userdata = {"name": rawUserData[:sepIndex], "entryCode": rawUserData[sepIndex+1:], "IP": addr}
    
    # Log connections
    print(str(addr) + time.strftime("   %H:%M:%S %Y-%m-%d", time.gmtime()))
    print(userdata)
    
    server.onClientConnect(userdata)
    
    if config["useEntryCode"]:
        if userdata["entryCode"]!=config["entryCode"]:
            c.send("deny".encode()) # Tell client access denied
            server.onClientEntryCodeFail(userdata)
            server.onClientDisconnect(userdata)
            c.close()
            print("Access denied with entry code: "+userdata["entryCode"]) # Log
            continue
    
    c.send("ok".encode()) # Tell client access allowed
    server.onClientEntryCodePass(userdata)
    
    # Decode received data
    line = (c.recv(2048)).decode("ASCII")
    cmd = line.split()[0]   # Command
    args = line.split()[1:] # Arguments
    
    print(line) # Log
    
    if REFUSE_CONNECTION:
        c.send(b"Connection refused")
        server.onClientDisconnect(userdata)
        c.close()
        continue
    
    # Execute commands    Check if command is valid, if file exists
    if os.path.isfile(CWD+"/shell/{}.py".format(cmd)):
        # Load file (command)
        f = open(CWD+"/shell/{}.py".format(cmd), 'r')
        code = f.read()
        f.close()
        if not DEBUG:
            try:
                server.onCommandStartExecute(userdata, cmd, args)
                exec(code, globals())  # Execute
                server.onCommandExecute(userdata, cmd, args)
            except:
                c.send(text["inError"].encode()) # Message if code failed to execute
                server.onCommandExecuteFail(userdata, cmd, args)
        else:
            server.onCommandStartExecute(userdata, cmd, args)
            exec(code, globals())  # Execute
            server.onCommandExecute(userdata, cmd, args)
    else:
        c.send(text["noCommand"].encode())
    # Disconnect
    server.onClientDisconnect(userdata)
    c.close()