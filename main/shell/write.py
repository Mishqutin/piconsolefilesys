path = userPath(args[0])
if fs.exists(path) and fs.type(path)=="directory":
    c.send("That's a directory!".encode())
else:
    code = ' '.join(args[1:])
    fs.writefile(path, code)