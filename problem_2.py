import os

filePaths = []

def walk(p, ext):
    if os.path.isdir(p):
        for dir in os.listdir(p):
            walk(p + '/' + dir, ext)
            # print(dir)
    elif os.path.isfile(p):
        _, fileExtension = os.path.splitext(p)
        if fileExtension == ext:
            filePaths.append(p)

    return filePaths



print(walk('./testdir', '.c'))