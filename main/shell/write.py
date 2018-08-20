if reqparam(2):
    path = userPath(args[0])
    if fs.exists(path) and fs.type(path)=="directory":
        sendmsg("That's a directory!")
    else:
        code = ' '.join(args[1:])
        fs.writefile(path, code)
else:
    sendmsg("Syntax error")