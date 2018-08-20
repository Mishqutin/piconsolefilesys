code = str(fs.filesystem)

f = open(CWD+"/FILESYSTEM", 'w')
f.write(code)
f.close()
c.send(b"File system saved!")