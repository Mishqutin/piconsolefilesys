if reqparam(1):
    path = userPath(' '.join(args))
    if not fs.exists(path) or not fs.type(path)=="file":
        sendmsg("No such file!")
    else:
        x = fs.readfile(path)
        sendmsg(x, 0)
else:
    sendmsg("Syntax error")