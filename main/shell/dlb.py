if reqparam(1):
    param = ' '.join(args)
    path = userPath(param)
    if not fs.exists(path) or fs.type(path)=="directory":
        sendmsg("No such file!")
    else:
        x = fs.readfile(path)
        uploadFile(osp.basename(param), x)
else:
    sendmsg("Syntax error")

