if reqparam(1):
    path = userPath(' '.join(args))
    if not fs.exists(path) or fs.type(path)=="directory":
        c.send("No such file!".encode())
    else:
        x = fs.readfile(path)
        c.send(x.encode())
else:
    c.send(b"Syntax error")