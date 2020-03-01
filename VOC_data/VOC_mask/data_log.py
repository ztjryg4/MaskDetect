def start(logname):
    import time
    localtime = time.strftime("-%Y-%m-%d-%H-%M-%S", time.localtime())
    filename = logname + localtime + ".txt"
    logfile = open(filename,"w+")
    return filename

def add(content,filename):
    logfile = open(filename,"a")
    logfile.write(content+"\n")