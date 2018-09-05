import maya.cmds as cmds


#返回Maya场景中外部文件的目录。
cmds.filePathEditor(query=True, listDirectories="")

#Return the directories of the external files that are saved at the target location.
#返回目标位置保存的外部文件的目录。
cmds.filePathEditor(query=True, listDirectories="c:/textures/", status=True)

#Return the files present in the specified directory, but not including the
#files in the sub directories.If no specified directory, search all external
#files in the scene.
#
#Use "withAttribute" to return the associated plugs.
#
#Use "status" to return whether the file exists.
#
#Use "unresolved" to return the broken files only.
#
#Use "attributeOnly" to return node and attribute name only.
#
#Use "byType" to specify the node and attribute type.
#
#For example, if "stone.jpg" exists and it is used by the plug
#"node1.imageName", then the returned result will be an ordered pair:
#"stone.jpg node1.imageName 1".
#
cmds.filePathEditor(query=True, listFiles="c:/textures/", withAttribute=True, status=True)
#
#If "rock.jpg" does not exists and it is used by the plug
#"node1.imageName", then this broken file and its plug
#can be found by the command.
#
cmds.filePathEditor(query=True, listFiles="", unresolved=True, withAttribute=True)
#Result: [u'rock.jpg', u'node1.imageName']
#
#List files that are used in the specified attribute of imagePlane
#
cmds.filePathEditor(query=True, listFiles="", byType="imagePlane.imageName")
#
#List all files that are used in the imagePlane node
#
cmds.filePathEditor(query=True, listFiles="", byType="imagePlane")
#
#Get all nodes or attributes that are using broken files to repath them
#
cmds.filePathEditor(query=True, listFiles="", unresolved=True, attributeOnly=True)
#
#Get the imagePlane file attributes that are using broken files to repath them
#
cmds.filePathEditor(query=True, listFiles="", unresolved=True, attributeOnly=True, byType="imagePlane.imageName")

#Return the label for the specified type.
#
#Strings are only guaranteed to be localized for the default types. For the
#other types, the strings are user-specified.
#
cmds.filePathEditor(query=True, typeLabel="imagePlane")

#Register and save a new file type and type label.
#
#These are persistent and can be used in future sessions.
#
cmds.filePathEditor(registerType="containerBase.iconName", typeLabel="ContainerIcon")

#Deregister a file type and clean the saved information.
#
cmds.filePathEditor(deregisterType="containerBase.iconName")

#Register a new non-persistent file type and type label.
#
cmds.filePathEditor(registerType="containerBase.iconName", typeLabel="ContainerIcon", temporary=True)

#Deregister a file type without affecting the persistent information.
#
cmds.filePathEditor(deregisterType="containerBase.iconName", temporary=True)

#Return all registered types, including default types.
#
cmds.filePathEditor(query=True, listRegisteredTypes=True)

#Query the attribute type for a plug instance.
#
cmds.filePathEditor("node1.fileTextureName", query=True, attributeType=True)

#Refresh all the file path editor's information for the current scene.
#
cmds.filePathEditor(refresh=True)

#Recursively look for files with the same name in the target directory. Repath
#the plugs value to those files.
#
#Use "force" to edit all the given plugs, even if the original path does not
#exist.
#
#Use "recursive" to find files recursively and to make sure the files do exist.
#
cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/",
						force=True, recursive=True)

#Preview the result of an operation without doing it.
#
#Returns the file name and whether the new file exists. This is returned as a
#list of pairs.
#
cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", repath="e:/textures/", preview=True)

#Replace strings in file paths.
#
#Here, the string "image" in the directory part will be replaced by "texture".
#
cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName", replaceField="pathOnly", replaceString=("image", "texture"), replaceAll=True)

#Copy a file from the source to the destination and repath the plug data to the new file.
#
#Use "force" to overwrite the file at the destination if it has a name clash.
#
cmds.filePathEditor("node1.fileTextureName", "node2.fileTextureName",  copyAndRepath=("e:/textures", "g:/image"), force=True)
	