import maya.cmds as cmds
cmds.sphere( n="sphere" )

# Set a simple numeric value
cmds.setAttr( 'sphere.translateX', 5 )

# Lock an attribute to prevent further modification
cmds.setAttr( 'sphere.translateX', lock=True )

# Make an attribute unkeyable
cmds.setAttr( 'sphere.translateZ', keyable=False )

# Set an entire list of multi-attribute values in one command
cmds.setAttr( 'sphereShape.weights[0:6]',1, 1, 2, 1, 1, 1, 2,size=7)
# Set an attribute with a compound numeric type
cmds.setAttr('sphere.rotate', 0, 45, 90, type="double3")

# Clamp the value of the attribute to the min/max
# Useful floating point math leaves the value just
# a little out of range - here the min is .01
cmds.setAttr( 'anisotropic1.roughness', 0.0099978, clamp=True )

# Set a multi-attribute with a compound numeric type
cmds.setAttr( 'sphereShape.controlPoints[0:2]', 0, 0, 0, 1, 1, 1, 2, 2, 2,type="double3" )