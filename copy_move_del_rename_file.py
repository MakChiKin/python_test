import maya.cmds as cmds

# Create a new directory path
#创建一个文件夹路径
cmds.sysFile( 'C:/temp/mayaStuff', makeDir=True )# Windows
cmds.sysFile( '/Users/makchikin/Downloads/MAYA/pythonTest/scenes/mayaStuff', makeDir=True )# Mac

# Move a scene to the new directory (we can rename it at the same time).
#移动一个文件,同时如果需要可以重命名
cmds.sysFile( 'C:/maya/projects/default/scenes/myScene.mb', rename='C:/temp/mayaStuff/myScene.mb.trash' )# Windows
cmds.sysFile( '/Users/makchikin/Downloads/MAYA/pythonTest/scenes/exp.ma', rename='/Users/makchikin/Downloads/MAYA/pythonTest/exp.ma.trash' )# Mac


# 重命名文件"myScene.will.be.deleted"
cmds.sysFile( 'C:/temp/mayaStuff/myScene.mb.trash', rename='C:/temp/mayaStuff/myScene.will.be.deleted' )# Windows
cmds.sysFile( '/tmp/mayaStuff/myScene.mb.trash', rename='/tmp/mayaStuff/myScene.will.be.deleted' )# Mac

# 复制文件到另一个文件夹
destWindows = "C:/temp/mayaStuff/myScene.mb.trash"
srcWindows = "C:/maya/projects/default/scenes/myScene.mb"
cmds.sysFile( srcWindows, copy=destWindows )# Windows

destMac = "/tmp/mayaStuff/myScene.mb.trash"
srcMac = "maya/projects/default/scenes/myScene.mb"
cmds.sysFile( srcMac, copy=destMac )# Mac

# 删除文件
cmds.sysFile( 'C:/temp/mayaStuff/myScene.will.be.deleted', delete=True )# Windows
cmds.sysFile( '/tmp/mayaStuff/myScene.will.be.deleted', delete=True )# Mac