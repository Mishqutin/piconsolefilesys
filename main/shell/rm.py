if reqparam(1):

    path = userPath(args[0])
    if fs.exists(path):
        fs.remove(path)
    else:
        c.send(b"Object doesn't exist!")
else:
    c.send(b"Synatax error")