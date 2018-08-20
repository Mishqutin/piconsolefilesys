if reqparam(1):

    path = userPath(args[0])
    if fs.exists(path):
        fs.remove(path)
    else:
        sendmsg("Object doesn't exist!")
else:
    sendmsg("Synatax error")