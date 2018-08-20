if reqparam(1):
    path = ' '.join(args)

    x = userPath(path)


    print(x)
    if x=="/":
        users[userdata["name"]]["dir"] = x
    elif fs.exists(x) and not fs.type(x)=="file":
        users[userdata["name"]]["dir"] = x
    else:
        sendmsg("No such directory!")

else:
    sendmsg("Syntax error")