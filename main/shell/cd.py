path = ' '.join(args)

x = userPath(path)


print(x)
if x=="/":
    users[userdata["name"]]["dir"] = x
elif fs.exists(x):
    users[userdata["name"]]["dir"] = x
else:
    c.send("No such directory!".encode())