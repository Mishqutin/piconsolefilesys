path = userPath(args[0])
if fs.exists(path):
    fs.remove(path)
else:
    c.send(b"Object doesn't exist!")