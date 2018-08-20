code = str(fs.filesystem)

f = open(CWD+"/FILESYSTEM", 'w')
f.write(code)
f.close()
sendmsg("File system saved!")