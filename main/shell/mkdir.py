if reqparam(1):
    path = userPath(' '.join(args))
    if fs.exists(path):
        sendmsg("Object already exists!")
    else:
        fs.makedir(path)
else:
    sendmsg("Syntax error")