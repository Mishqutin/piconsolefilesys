
DEBUG = 1



f = open(CWD+"/FILESYSTEM", 'r')
code = eval(f.read())
f.close()

filesystem = code


class filesys:
    def __init__(self, sys={}):
        self.filesystem = sys
    
    def path(string):
        path = "self.filesystem"
        if string[0]=="/": string = string[1:]
        for i in string.split("/"):
            if i=="": continue
            path = path+"['{}']['content']".format(i)
        return path
    
    def pathobj(string):
        path = "self.filesystem"
        if string[0]=="/": string = string[1:]
        c = 1
        for i in string.split("/"):
            if c==len(string.split("/")):
                path = path+"['{}']".format(i)
            else:
                path = path+"['{}']['content']".format(i)
            c+=1
        return path
    
    def exists(self, path):
        if path=="/": return True
        try:
            x = eval(filesys.pathobj(path)+"['type']")
            return True
        except:
            return False
    
    def type(self, path):
        if path=="/": return "directory"
        return eval(filesys.pathobj(path)+"['type']")
    
    def readfile(self, path):
        return eval(filesys.path(path))
    
    def writefile(self, path, content):
        exec( filesys.pathobj(path)+" = {'type': 'file', 'content': content }", locals() )
    
    def writefilebytes(self, path, content):
        exec( filesys.pathobj(path)+" = {'type': 'bytefile', 'content': content }", locals() )
    
    def remove(self, path):
        exec( "del "+filesys.pathobj(path), locals() )
    
    def makedir(self, path):
        exec( filesys.pathobj(path)+" = {'type': 'directory', 'content': {} }", locals() )
    
    def listdir(self, path):
        if path=="/":
            dir = eval("self.filesystem")
        else:
            dir = eval(filesys.path(path))
        l = []
        for i in dir:
            l.append(i)
        return l

fs = filesys(filesystem)
