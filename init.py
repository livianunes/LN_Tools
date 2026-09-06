#IMPORTS::::::::::::::::::::::::::::::
import nuke
import inspect
import os

#LIVIA_NUNES_TOOLS_PATHS::::::::::::::::::::::::::::::

#Gets current path of this module
thisPath = inspect.getabsfile(inspect.currentframe())
thisFolder = os.path.dirname(thisPath)
#Finds subdirs
subdirs = [x[0] for x in os.walk(thisFolder)]
#removes this dir
subdirs.remove(thisFolder)
#Adds any subdirs to nuke plugin path
for i in subdirs:
    nuke.pluginAddPath(i)
