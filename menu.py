#IMPORTS::::::::::::::::::::::::::::::::::::::::::::::
import os
import inspect
import nuke

#LIVIA_NUNES_TOOLS_ADD_TO_MENU::::::::::::::::::::::::::::::

#root directory name for tools collection
rootToolsDir = "tools"

#Gets current path of this module
thisPath = inspect.getabsfile(inspect.currentframe())
thisFolder = os.path.dirname(thisPath)
thisFolder = thisFolder.replace("\\","/")
#Set tools subdir
toolsDir = thisFolder+'/'+rootToolsDir+'/'

#Finds files in subdir
tools = []
for (dirpath, dirnames, filenames) in os.walk(toolsDir):
    if filenames != []:
        for file in filenames:
            name = dirpath.split('/')
            dirName = name[-2]
            subDirName = dirnames
            if dirName == rootToolsDir:
                tools.append(file)
            elif subDirName == rootToolsDir:
                tools.append(dirName+"/"+file)
                print((dirName+"/"+file))
            else:
                tools.append(subDirName+"/"+dirName+"/"+file)
                print((subDirName+"/"+dirName+"/"+file))

#list of tool paths
toolPaths = []
for tool in tools:
    toolPath = toolsDir+tool
    toolPaths.append(toolPath)

#list of tool names
toolNames = []
for file in tools:
    idx = file.find('.nk')
    name = file[0:idx]
    toolNames.append(name)

#create dictionary where key is toolname and value is toolpath
to_zip = list(zip(toolNames, toolPaths))
toolsDict = dict(to_zip)

#load toolset function
def loadTool(toolFullPath):
    nuke.loadToolset(toolFullPath)

#add general menu
LN_Tools_Menu = nuke.toolbar("Nodes").addMenu('LN_Tools', icon="LNToolsMenu.jpg")

#add menu function
def addToolToMenu(toolName, runTool):
    mNodes = nuke.menu('Nodes')
    mNodes.addCommand('LN_Tools/'+toolName, runTool)

#create all menus
for toolN in toolsDict:
    loadtoolset = "loadTool('"+toolsDict[toolN]+"')"
    addToolToMenu(toolName= toolN, runTool=loadtoolset)
