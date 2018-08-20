f = open(CWD+"/FILESYSTEM", 'r')
code = eval(f.read())
f.close()

fs.filesystem = code

sendmsg("File system loaded!")