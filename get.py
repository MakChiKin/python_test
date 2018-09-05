import maya.cmds as cmds

cmds.createNode( 'revolve', n='gravityWell' )
cmds.sphere( n='loxTank' )
cmds.cone( n='noseCone' )
cmds.cone( n='fin' )
cmds.pointConstraint( 'fin', 'noseCone', n='weld' )

angle = cmds.getAttr('gravityWell.esw')
# Result: 360 #
type = cmds.getAttr('loxTank.translate',type=True)
# Result: double3 #
lock = cmds.getAttr('noseCone.translateX',lock=True)
# Result: 0 #
finZ = cmds.getAttr('fin.translateZ',time=12)
# Result: 0.0 #
size = cmds.getAttr('weld.target',size=True)
# Result: 1 #
size = cmds.getAttr('weld.target',settable=True)
# Result: 0 #
matrix = cmds.getAttr('loxTank.matrix')
# Result: 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 1.0 #
cmds.createNode('file',n='file1')
cmds.setAttr( 'file1.ftn', '$TMPDIR/smile.gif',type='string' )
s = cmds.getAttr('file1.ftn')
# Result: $TMPDIR/smile.gif #
s = cmds.getAttr('file1.ftn',x=True)
# Result: /var/tmp/smile.gif #

# Get the list of all used indices on a multi attribute
cmds.getAttr('initialShadingGroup.dagSetMembers', multiIndices=True)
# Result: [0, 1, 2] #