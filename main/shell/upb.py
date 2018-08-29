c.send( ("#//upload " + args[0]).encode() )

c.send(b"ok")

print("Downloading file:" + args[0])

code = downloadFile()

fs.writefilebytes(userPath(args[0]), code)


print("File written")