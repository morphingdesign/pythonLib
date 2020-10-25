import os

def createPyDir(parentDir):
    """Create subdirectory structure within the user-created parent directory."""

    newDirs = ['bin', 'data', 'tools', 'ui', 'utils']

    newInitName = '__init__.py'
    for dr in newDirs:
        dirWPath = os.path.join(parentDir, dr)
        #print(dirWPath)
        os.mkdir(dirWPath)
        #print(dirWPath + '\\' + newInitName)
        newInitFile = open((dirWPath + '\\' + newInitName), "w")


