import maya.cmds as cmds

#创建一些对象和添加它们的集合 
cmds.sphere( n='sphere1' )
cmds.sphere( n='sphere2' )
cmds.sets( 'sphere1', 'sphere2', n='set1' )

#选择所有dag对象和所有依赖关系节点
cmds.select( all=True )

# 取消选择
cmds.select( clear=True )

# 只有在可见时才选择sphere2
cmds.select( 'sphere2', visible=True )

# 无论可见性如何，都要选择几个对象
cmds.select( 'sphere1', r=True )
cmds.select( 'sphere2', add=True )

# 从选中列表中取消其中一个球的选择
cmds.select( 'sphere1', tgl=True )

# 从选中列表中取消其中一个球的选择
cmds.select( 'sphere2', d=True )

# 以下选择set1的所有成员
cmds.select( 'set1' )

# 选择set它自己
cmds.select( 'set1', ne=True )


# 选择命名空间的一些示例

# 在命名空间中创建命名空间和对象
cmds.namespace( add='foo' )
cmds.namespace( set='foo' )
cmds.sphere( n='bar' )

# 'select bar' will not select "bar" unless bar is in the
# root namespace. You need to qualify the name with the
# namespace (shown below).
cmds.select( 'foo:bar*' )

# select all the objects in a namespace
cmds.select( 'foo:*' )


cmds.selectMode( object=True )
cmds.selectMode( q=True, component=True )
