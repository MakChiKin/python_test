#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8 
#encoding utf-8
import maya.cmds as cmds

#删除所有没有赋上模型的材质球和贴图节点
mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')  


#选模型
#查询所有在geometry的列表
geo = cmds.ls( type='geometryShape')
#选择列表中的模型
cmds.select(geo)
#向上一级选择
cmds.pickWalk(d="up")
#把选择的物体成为列表
all_geometry =cmds.ls(sl=True)
print len(all_geometry)

for i in all_geometry:
    print i

# 顶点数和面数的格式化查询
cmds.polyEvaluate( v=True, f=True, fmt=True )
# Result: "face=16 vertex=25"
#查询非4边面模型






#查询reference文件是否存在



#写界面



#通信





#查找丢失贴图
def findExistTextrue():
    #根据file节点查找贴图是否为空
    imageFiles = cmds.ls( type='file')
    #创建一个集合，把丢失贴图的图片file节点放在里面
    #没有路径的节点
    undefinedPathSel=[]
    #文件不存在的节点
    nonExistLocal=[]
    #文件不存在于sourceimages文件夹中
    nonExistSourceiamges=[]
    for i in imageFiles:
        #获取每个节点文件路径
        fileTexturePath= cmds.getAttr(i+'.fileTextureName')
        #判断文件路径是否存在
        exist = cmds.file( fileTexturePath, query=True, exists=True ) 
        #这个路径为空，则加载入undefinedPathSel
        if fileTexturePath=='':
            undefinedPathSel.append(i)
        #如果这个路径的文件不存在本地则加入
        elif not exist:
            nonExistLocal.append(i)
        #如果文件路径不存在sourceImages文件夹则放入nonExistSourceiamges
        elif not ('sourceimages' in fileTexturePath):
            nonExistSourceiamges.append(i)

    findExistTexMessage(undefinedPathSel,'此节点丢失贴图:')
    findExistTexMessage(nonExistLocal,'此节点贴图不存在:')
    findExistTexMessage(nonExistSourceiamges,'此节点贴图不存在sourceimage路径下:')
    #如果都没有节点，证明材质贴图没有问题
    if len(undefinedPathSel)!=0 and len(nonExistLocal)!=0 and len(nonExistSourceiamges)!=0:
        print '检查完毕，该文件材质贴图状态正常'

        
#打印查找信息    
def findExistTexMessage(sel,sen):
    if len(sel)>0:
        for i in sel:
            print sen,i
        



findExistTextrue()


#查询节点外部文件夹路径，如果listDirectories属性为“”，默认返回全部文件路径
listDirectories = cmds.filePathEditor(query=True, listDirectories="")
#查询节点外部文件路径，如果listFiles属性为“”，默认返回全部文件路径
listFiles = cmds.filePathEditor(query=True, listFiles="", byType="file")
print listDirectories
print listFiles



