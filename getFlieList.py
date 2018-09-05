import maya.cmds as cmds

# List the contents of the user's projects directory
#列出用户项目目录的名称
cmds.getFileList( folder=cmds.internalVar(userWorkspaceDir=True) )

# List all MEL files in the user's script directory
#列出用户脚本目录中的所有MEL文件
cmds.getFileList( folder=cmds.internalVar(userScriptDir=True), filespec='*.mel' )