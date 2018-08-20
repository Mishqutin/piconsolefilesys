f = open(CWD+"/FILESYSTEM", 'r')
code = eval(f.read())
f.close()

fs.filesystem = code

c.send(b"File system loaded!")