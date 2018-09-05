import maya.cmds as cmds

#将自动保存之间的间隔设置为5分钟
cmds.autoSave( int=300 )

# 查询自动保存间隔
cmds.autoSave( q=True, int=True )
# Result: 300.0 #