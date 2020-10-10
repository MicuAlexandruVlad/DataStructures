import os

filePaths = []

def walk(p):
    if os.path.isdir(p):
        for dir in os.listdir(p):
            walk(p + '/' + dir)
            # print(dir)
    elif os.path.isfile(p):
        _, fileExtension = os.path.splitext(p)
        if fileExtension == '.c':
            filePaths.append(p)

    return filePaths



print(walk('./testdir'))