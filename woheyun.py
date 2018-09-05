#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8 
#encoding utf-8
import maya.cmds as cmds
import maya.mel as mel
import urllib2,json,re

def separator_delimiter():
    print '---------------------------------------------------------\n'

 #提示窗口                    
def prompt(msg):
    cmds.confirmDialog (t ="Prompt", m= "%s" %msg ,b='OK')  
     
#提示窗口
def PromptWindow(titleText,contentText):
    form = cmds.setParent(q=True)
    cmds.formLayout(form, e=True)
    title = cmds.text(l='%s' %titleText ,align='left')
    content = cmds.text(align='left',hyperlink=1,l='%s' %contentText)
    button = cmds.button(l='OK', c='cmds.layoutDialog( dismiss="OK" )' )

    cmds.formLayout(form, edit=True,
                    attachForm=[
                        (title, 'top', 15), 
                        (title, 'left', 20), 
                        (content, 'top', 35), 
                        (content, 'left', 20), 
                        (button, 'bottom', 10),
                        (button, 'right', 20),
                        ],
                     attachControl=[
                         (content, 'bottom', 20, button)],
                        )

#删除所有没有赋上模型的材质球和贴图节点
def delUnusedNode(*arg):
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')  
 
#选polygon
def selcetPoly(*arg):
    polyList = []
    #查询所有在mesh的列表
    #geo = cmds.ls( type='geometryShape')
    mesh = cmds.ls( type='mesh')
    if len(mesh)>0:
        #选择列表中的模型
        cmds.select(mesh)
        #向上一级选择
        cmds.pickWalk(d="up")
        #把选择的物体成为列表
        polygon =cmds.ls(sl=True)
        #print len(polygon)
        for i in polygon:
            polyList.append(i)
        return polyList
    else :
        Prompt('No mesh in scene. ')
 
#查询模型和材质的关系
def model_mat_Relationship(miss_multiMat):
    #缺失材质数组
    missMat = []
    #多维材质数组
    multiMat = []
    #执行函数
    selcetPoly()
    cheakModel = cmds.ls(sl=1)
    for model in cheakModel:
        #print model #模型
        meshShape = cmds.ls(model,s=1,o=1,dag=1)
        #print meshShape #模型meshShape
        shadingGrps= cmds.listConnections(meshShape[0],type="shadingEngine")
        #print shadingGrps  #材质shape
        #如果为空这个对象没有材质
        if shadingGrps == None:    
           missMat.append(model)
        #如果大于1，则表示模型有多个材质球   
        elif len(shadingGrps) > 1:
           multiMat.append(model)
    #如果传入参数为0，则返回missMat
    if miss_multiMat == 0:  
        return missMat
    #如果传入参数为1，则返回multiMat
    if miss_multiMat == 1:   
        return multiMat
    
#处理材质模型关系
def cheakMat(type,selName,sentance1,sentance2):
    cmds.scriptEditorInfo(clearHistory=True)
    shadingGrps=[]
    shadingGrps = model_mat_Relationship(type)
    #print shadingGrps
    #如有丢失材质球
    if  len(shadingGrps) > 0:
        #判断是否存在对应的集合 missMatSel/multimatSel
        existSel = cmds.ls(selName,type="objectSet")
        #如不存在，创建集合并加入集合
        if len(existSel) == 0 :  
            cmds.select(shadingGrps) 
            createSet = cmds.sets (name = selName)
        #如存在添加到集合   
        if len(existSel) != 0:
            cmds.sets(shadingGrps,add=selName)
        cmds.select(cl=1)
        cmds.select(shadingGrps)
        print sentance1
        separator_delimiter()
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('Check Finished.','%s')"%sentance1)  
    else :
        cmds.select(cl=1)
        print sentance2
        separator_delimiter()
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('Check Finished.','%s')"%sentance2)
 
#处理缺失材质模型
def cheakMissMat(*arg):
    cheakMat(0,'missMatSel','These are some models without material.',"Great! No models with missing materials.")
 
#检查多维材质模型
def cheakMultiMat(*arg):
    cheakMat(1,'multimatSel','These models have multiple materials.',"No relevant models were found.") 
 
#查找丢失贴图
def checkTexExist(*arg):
    #根据file节点查找贴图是否为空
    imageFiles = cmds.ls( type='file')
    if len(imageFiles)>0:
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

        if len(undefinedPathSel)>0:findExistTexMsg(undefinedPathSel,u'此节点丢失贴图:')
        if len(nonExistLocal)>0:findExistTexMsg(nonExistLocal,u'此节点贴图已丢失不存在:')
        if len(nonExistSourceiamges)>0:findExistTexMsg(nonExistSourceiamges,u'此节点贴图不存在sourceimage路径下:')
        #如果都没有节点，证明材质贴图没有问题
        if len(undefinedPathSel)==0 and len(nonExistLocal)==0 and len(nonExistSourceiamges)==0:
            cmds.scriptEditorInfo(clearHistory=True)
            print 'Check finished. The file texture mapping status is normal.'
            cmds.layoutDialog(t='Prompt',ui="PromptWindow('Check Finished','All file texture mapping status is normal.')")
            separator_delimiter()
    else:
        #Prompt('No texture file in scene.')
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('Check Finished','No texture file in scene.')")
        separator_delimiter()
      
#打印查找信息    
def findExistTexMsg(sel,sen):
    if len(sel)>0:
        fileNodeSel = ''
        for i in range(len(sel)):
            print sen,sel[i]
            fileNodeSel = fileNodeSel+sel[i]+'\\n'
        separator_delimiter()
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('%s','%s')"%(sen,fileNodeSel))
       
#查询本地场景中所有reference路径
def checkRefExist(*arg):
    #cmds.scriptEditorInfo(clearHistory=True)
    referencePathSet = []
    unExistRefPathSet = []
    referencePathSet = cmds.file( query=True, list=True )
    #print referencePathSet
    for i in referencePathSet:
        #判断文件路径是否存在
        #print i
        referenceExist = cmds.file( i, query=True, exists=True )
        if not referenceExist:
            #不存在的路径文件存放于此数组
            unExistRefPathSet.append(i)
    
    #检查数组是否存在路径，如没有表示祝贺，如有打印所有路径         
    if len(unExistRefPathSet) == 0:
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('Info','Great! The system files are complete.')")
        separator_delimiter()
    else:
        pathSel=''
        for i in range(len(unExistRefPathSet)):
            pathSel = pathSel+unExistRefPathSet[i]+'\\n'
        print pathSel
        cmds.layoutDialog(t='Prompt',ui="PromptWindow('These reference file does not exist and please check paths:','%s')"%pathSel)
        separator_delimiter()
  
#检查模型面数
def checkFaceNum(*arg):
    noFace=[]
    faceMore4=[]
    selcetPoly()
    ploygon = cmds.ls(sl=1)
    #print ploygon
    for i in ploygon:
        cmds.select(cl=1)
        cmds.select(i)
        # 顶点数和三角面数的查询
        count = cmds.polyEvaluate()
        triangleCount = count['triangle']
        vertexCount = count['vertex']
    
        #如三角面数等于0或者顶点数小于等于2，则加入数组
        if triangleCount == 0 or vertexCount <= 2 :
            noFace.append(i)
            
    if len(noFace)>0:
        #print noFace
        cmds.select(noFace)
        cmds.layoutDialog(t='Prompt',ui=("PromptWindow('Check Finished','Selected models with problems，Please Cheak!')"))
    else:
        cmds.select(cl=1)
        cmds.scriptEditorInfo(clearHistory=True)
        #cmds.inViewMessage( amg='所有模型 <hl>正常</hl>.', pos='midCenter', fade=True )
        cmds.layoutDialog(t='Prompt',ui=("PromptWindow('Check Finished','All models are normal.')"))
        print 'All models are normal.'
        separator_delimiter()
 
                                                                                                                         
#POST                     
def requsetURL(*arg):
    url = 'https://cs.woheyun.com/api/cgwas/uploadFileAction/getUploadFileUrl.json'
    req = urllib2.Request(url)
    jsonData = urllib2.urlopen(req).read()
    jsonText = json.loads(jsonData)
    print jsonText
    url = jsonText['data']['postObjectPolicy']['host']
    key = jsonText['data']['postObjectPolicy']['dir'] + '${filename}'
    policy = jsonText['data']['postObjectPolicy']['policy']
    OSSAccessKeyId = jsonText['data']['postObjectPolicy']['accessid']
    signature = jsonText['data']['postObjectPolicy']['signature']
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
    params = {"key": (None, "%s" % key),
              "policy": (None, "%s" % policy),
              "OSSAccessKeyId": (None, "%s" % OSSAccessKeyId),
              "success_action_status": (None, "200"),
              "signature": (None, "%s" % signature),
              "file": ('test03.zip', open('/Users/makchikin/Downloads/test03.zip', 'rb'), 'application/zip')
              }
    return url,params,headers
 
def POST_01(*arg):
    jsonText = requsetURL()
    files=MultipartEncoder(jsonText[1])
    #方法1
    res = requests.post(jsonText[0],files,jsonText[2])
    #print res.request.headers
    print res.request.body
    if res.status_code==200:
        print '>>>success'
    else:
        print '>>>failed'
        print res.status_code
        print res.content

def POST_02(*arg):
    jsonText = requsetURL()
    #data = " ".join(jsonText[1])
    #print data
    # response = requests.post(url,files=data)
    data = json.dumps(jsonText[1])
    req = urllib2.Request(jsonText[0],data,jsonText[2])
    res = urllib2.urlopen(req)
    res = res.read()
    print res

#执行发送文件
def sendCloud(*arg):
    POST_02()
    
    
#跳转官网
def visitHomePage(*arg):      
    cmds.showHelp('https://www.woheyun.com/#/',absolute=True)           



#Tab
def modelTab(*arg):
    #check model 
    cmds.columnLayout( adjustableColumn=True )#01
    
    cmds.frameLayout( label='Check Tools',cll=1,cl = 0,w=290)#001
    cmds.columnLayout() 
    cmds.button(l='Check Model',bgc=(0.42,0.42,0.42),w=290,c=checkFaceNum)
    cmds.button(l='Cheak Miss Materials',bgc=(0.42,0.42,0.42),w=290,c=cheakMissMat )
    cmds.button(l='Cheak Multimaterials',bgc=(0.42,0.42,0.42),w=290,c=cheakMultiMat)
    cmds.button(l='Check Texture Exist',bgc=(0.42,0.42,0.42),w=290,c=checkTexExist)
    cmds.button(l='Check Reference Path',bgc=(0.42,0.42,0.42),w=290,c=checkRefExist)
    cmds.setParent( '..' )
    cmds.setParent( '..' )#001
    
    cmds.frameLayout( label='Cloud rendering',cll=1,cl = 0,w=290)#002
    cmds.columnLayout() 
    cmds.button(l='Send',bgc=(0.42,0.42,0.42),w=290,c=sendCloud)
    cmds.setParent( '..' )
    cmds.setParent( '..' )#002
    
    cmds.setParent( '..' )#01

def animationTab(*arg):
    cmds.frameLayout( label='Binding Tool',cll=1,cl = 0,w=290)
    cmds.columnLayout() 
    cmds.button()
    cmds.setParent( '..' )
    cmds.setParent( '..' )

def renderingTab(*arg):
    cmds.frameLayout( label='Aronld',cll=1,cl = 0,w=290)
    cmds.columnLayout() 
    cmds.button()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
    cmds.frameLayout( label='Red Shift',cll=1,cl = 0,w=290)
    cmds.columnLayout() 
    cmds.button()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
    
def dynamicTab(*arg):
    cmds.frameLayout( label='FX',cll=1,cl = 0,w=290)
    cmds.columnLayout() 
    cmds.button()
    cmds.setParent( '..' )
    cmds.setParent( '..' )
 
#UI
try:
    if cmds.window(mainwindow,ex=True):
       cmds.deleteUI(mainwindow,wnd=True)
       cmds.deleteUI(checkTools,wnd=True)
except:
    #print 'Nothing mainWindow'
    cmds.scriptEditorInfo(clearHistory=True)

 
mainwindow = cmds.window(title="WoHeYun",mnb =True ,mxb = False,sizeable=0)
mainLayout=cmds.columnLayout(w=250,h=340)
cmds.columnLayout(h=90,bgc=(0,0,0))
cmds.symbolButton(enable=1, command=visitHomePage,image="icons/woheyunlogo.png",ann='www.woheyun.com')
cmds.setParent( '..' )
cmds.text (l='www.woheyun.com',h=15,w=289,fn='boldLabelFont',bgc=(0.15,0.15,0.15))#


cmds.columnLayout( adjustableColumn=True ,w=250)
menuBarLayout = cmds.menuBarLayout()
cmds.menu( label='File' )
cmds.menuItem( label='Batch render setting' )
cmds.menu( label='Help', helpMenu=True )
cmds.menuItem( label='About...' )
cmds.setParent( '..' )
cmds.setParent( '..' )


cmds.columnLayout( adjustableColumn=True ,w=290)
form = cmds.formLayout()
tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', -5), (tabs, 'bottom', 0), (tabs, 'right', -5)) )

model = cmds.rowColumnLayout(numberOfColumns=2)
modelTab()
cmds.setParent( '..' )

animation = cmds.rowColumnLayout(numberOfColumns=2)
animationTab()
cmds.setParent( '..' )

rendering = cmds.rowColumnLayout(numberOfColumns=2)
renderingTab()
cmds.setParent( '..' )

dynamic = cmds.rowColumnLayout(numberOfColumns=2)
dynamicTab()
cmds.setParent( '..' )

cmds.tabLayout( tabs, edit=True, tabLabel=((model, 'Model'), (animation, 'Animation'),(rendering, 'Render'), (dynamic, 'Dynamic')) )
cmds.setParent( '..' )


cmds.showWindow( mainwindow )

 
 
 
 
    
 
 
 
 
 
 
 
 


