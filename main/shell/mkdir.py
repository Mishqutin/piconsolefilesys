path = userPath(' '.join(args))
if fs.exists(path):
    c.send("Object already exists!".encode())
else:
    fs.makedir(path)