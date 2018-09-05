import maya.cmds as cmds

#例5 保存、打开、引用和查询引用路径
#保存当前文件为ma文件
cmds.file( rename='fred.ma' )
cmds.file( save=True, type='mayaAscii' )
#保存当前文件为mb文件
cmds.file( rename='fred.mb' )
cmds.file( save=True, type='mayaBinary' )


#保存当前场景为非ma扩展的文件，保存出来为mb文件
cmds.file( rename='tmp' )
cmds.file( save=True, defaultExtensions=False, type='mayaAscii' )


#打开文件
cmds.file( 'fred.ma', open=True )

# reference the file wilma.mb
#引用文件
cmds.file( 'C:/mystuff/wilma.mb', reference=True )


#查询该文件下的引用节点
cmds.file( 'C:/mystuff/wilma.mb', query=True, referenceNode=True )
# Result: wilmaRN #


#查询wilmaRN节点是否延期引用
cmds.file(query=True, referenceNode='wilmaRN', deferReference=True)
# Result: False #


#引用文件并命名该引用的命名空间
cmds.file( 'C:/maya/projects/default/scenes/barney.ma', reference=True, type='mayaAscii', namespace='rubble' )


#修改引用文件的命名空间
cmds.file( 'C:/maya/projects/default/scenes/barney.ma', edit=True, namespace='purpleDinosaur' )


#查询场景中所有reference路径
cmds.file( query=True, list=True )
# Result: C:/maya/projects/default/scenes/fred.ma C:/mystuff/wilma.mb C:/maya/projects/default/scenes/barney.ma

# Select "betty" and export betty to a separate file called "betty.mb".
# Reference the new betty file into this scene, replacing the
# previous betty object from this scene with the reference to betty.
#
cmds.file( 'c:/mystuff/betty.mb', type='mayaBinary', namespace='rubble', exportAsReference=True )


#选择与文件betty.mb关联的所有对象
cmds.file( 'c:/mystuff/betty.mb', selectAll=True )
# Result: rubble:betty


#从场景中移除所有相关该文件的引用节点
cmds.file( 'c:/mystuff/betty.mb', removeReference=True )


#查询改路径下是否已经存在该文件
cmds.file( 'foo.mb', query=True, exists=True )
# Result: 0 #


# 查询引用节点"rubble:betty“是否为延期加载，注意, -referenceNode 指令必须放在 -q 指令前.
cmds.file(referenceNode='rubbleRN', query=True, deferReference=True )


#查询在保存文件间最后后一个临时文件
cmds.file( query=True, lastTempFile=True)

####################################/
#/   Example for the '-buildLoadSettings' and '-loadSettings' flags  #/
####################################/

# Build load settings for "ref.ma"
cmds.file( 'ref.ma', open=True, buildLoadSettings=True )
# Edit those settings, to indicate that some reference should
# be brought in unloaded.
# Note: the following command is primarily intended for internal
# use. It may not be easy to determine the numeric ID of a given
# reference ("2" in this case) .
# cmds.loadSettings( '2', deferReference=1 )
# Use the edited settings when opening the file
cmds.file('ref.ma', open=True, loadSettings='implicitLoadSettings')

#
#   Example for the '-cleanReference' and '-editCommand' flags
#


#创建一个简单的引用球体
cmds.file( force=True, new=True )
cmds.polySphere()
cmds.file( rename='ref.ma' )
cmds.file( force=True, type='mayaAscii', save=True )
cmds.file( force=True, new=True )
cmds.file( 'ref.ma', reference=True, namespace='ref' )

#放大球体，设置属性，或获取属性
cmds.setAttr( 'ref:pSphere1.s', 5, 5, 5 )
cmds.getAttr( 'ref:pSphere1.s' )
# Result: 5 5 5 #

# The 'cleanReference' and 'editCommand' flags only work on
#不加载引用
cmds.file( unloadReference='refRN' )

#查询已经修改过的对象
cmds.reference( referenceNode='refRN', query=True, editCommand=True )
# Result: setAttr ref:pSphere1.s -type "double3" 5 5 5 setAttr ref:lightLinker1.lnk -s 2 #

# Remove all setAttr edits on refRN:
#移除所有编辑过的引用对象节点
cmds.file( cleanReference='refRN', editCommand='setAttr' )
cmds.reference( referenceNode='refRN', query=True, editCommand=True )
#注意这里没有反馈

#加载引用
cmds.file( loadReference='refRN' )
#再次查看物体属性，发现之前物体的修改，已经全部没有了
cmds.getAttr( 'ref:pSphere1.s' )
# Result: 1 1 1 #
# Note that scale has returned to 1 1 1

# 将编辑文件应用于引用
cmds.file("translateSphere.editMA", reference=True, applyTo="refRN")
# Result: maps <main> to refRN's namespace

# 将编辑文件应用于主场景中的节点
cmds.file("translateSphere.editMA", i=True, applyTo=":")
# Result: maps <main> to the root namespace

# 将编辑文件应用于引用，但它也有两个引用之间的连接
cmds.file("connectionsBetweenRefs.editMA", reference=True, applyTo="refRN", mapPlaceHolderNamespace=("<otherRef>", "otherRefRN"))
# Result: maps <main> to refRN's namespace and <otherRef> to otherRefRN's namespace

# 改变文件的修改状态
cmds.file(modified=True)

# 设置文件选项
cmds.file( force=True, save=True, options='v=1;p=17',type='mayaAscii');
# Result:The saved file uses full names for attributes on nodes and flags in command.Also the precision of values in file is 17.
#设置/查询当前设置的文件选项。保存maya文件时使用文件选项。当前文件命令支持的两个文件选项标志是v和p。
#v（详细）指示在保存文件时是使用长属性名称还是短属性名称和命令标志名称。由maya ascii和maya二进制文件格式使用。
#它只能是0或1。
#设置v = 1表示将使用长属性名称和命令标志名称。默认情况下，或通过设置v = 0，将使用短属性名称。
#p（precision）定义了保存文件时maya文件IO的精度。仅由maya ascii文件格式使用。
#它是一个整数值。默认值为17。
#选项格式为“flag1 = XXX; flag2 = XXX”.Maya使用最后一个v和p作为最终结果。



# 加载 Reference 预览

# 在父引用下使用子引用创建嵌套引用。
cmds.file( force=True, new=True )
cmds.polySphere()
cmds.file( rename='child.ma' )
cmds.file( force=True, type='mayaAscii', save=True )
cmds.file( force=True, new=True )
cmds.file( 'child.ma', reference=True, namespace='child_namespace' )
cmds.file( rename='parent.ma' )
cmds.file( force=True, type='mayaAscii', save=True )

# 在卸载的父引用下预览卸载的子引用。
cmds.file( force=True, new=True )
cmds.file( 'parent.ma', reference=True, namespace='parent_namespace' )
cmds.file( 'parent.ma', unloadReference=True )
cmds.file( 'parent.ma', loadReferencePreview=True )

#
#			   Example for 'mergeNamespacesOnClash'
#

# 创建一个引用
cmds.file( force=True, new=True )
cmds.namespace( add="bar" )
cmds.namespace( set="bar" )
cmds.polySphere();
cmds.file( rename="ref.ma" )
cmds.file( force=True, type='mayaAscii', save=True )

# 创建一些名称空间和对象创建在场景中
cmds.file( force=True, new=True )
cmds.namespace( add="ref:foo:bar" )
cmds.namespace( set="ref:foo:bar" )
cmds.polySphere();

# 合并到 root
cmds.file('ref.ma', reference=True, mergeNamespacesOnClash=True, namespace=':');

# 合并到嵌套命名空间':ref:foo'
cmds.file('ref.ma', i=True, mergeNamespacesOnClash=True, namespace=':ref:foo');

# 不合并命名空间
cmds.file('ref.ma', reference=True, mergeNamespacesOnClash=False, namespace=':ref:foo');

#现在编辑新命名空间并合并它
cmds.file('ref.ma', edit=True, mergeNamespacesOnClash=True, namespace=':ref:foo');




###############################################/
#/ Example for export with relativeNamespace  #/
###############################################/

cmds.file(new=True,force=True)
cmds.sphere(name=":A:sphereA")
cmds.sphere(name=":A:B:sphereB")
cmds.sphere(name=":A:B:C:sphereC")
cmds.sphere(name=":D:sphereD")

# Select all the spheres.
#
cmds.select(":A:sphereA", replace=True)
cmds.select(":A:B:sphereB",add=True)
cmds.select(":A:B:C:sphereC",add=True)
cmds.select(":D:sphereD",add=True)


#使用-relativeNamespace指令导出所有这些球体，该文件为ma文件。
cmds.file(rename="exp.ma")
cmds.file(force=True, exportSelected=True, type="mayaAscii", relativeNamespace=":A:B")
# The result in the exported file:
# :A:sphereA
# :C:sphereC
# :D:sphereD
# -sphereB