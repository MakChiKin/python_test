import maya.cmds as cmds

cmds.polyPlane( n='plg', sx=4, sy=4, w=5, h=5 )
cmds.select( 'plg.f[2]', 'plg.f[4]' )

#  查询面数
cmds.polyEvaluate( f=True )
# Result: 16

# 查询三角面数
cmds.polyEvaluate( t=True )
# Result: 32

# 查询选择面的数量
cmds.polyEvaluate( faceComponent=True )
# Result: 2

# 查询顶点和面的数量
cmds.polyEvaluate( v=True, f=True )
# Result: {'vertex': 25, 'face': 16}

# 顶点数和面数的格式化查询
cmds.polyEvaluate( v=True, f=True, fmt=True )
# Result: "face=16 vertex=25"

# 查询所有：边 边组件 面 面组件 壳 三角形 三角形组件 uv uv组件 uv壳 uvCood 顶点 顶点组件
cmds.polyEvaluate()
# Result: {'edge': 40, 'edgeComponent': 0, 'face': 16, 'faceComponent': 2, 'shell': 1, 'triangle': 32, 'triangleComponent': 0, 'uvComponent': 0, 'uvShell': 1, 'uvcoord': 25, 'vertex': 25,'vertexComponent': 0}

#格式化所有信息
cmds.polyEvaluate( fmt=True )
# Result: vertex=25 edge=40 face=16 uvcoord=25 triangle=32 shell=1 uvShell=1
#    vertexComponent=0 edgeComponent=0 faceComponent=2 uvComponent=0
#    triangleComponent=4 activeShells= 0 activeUVShells= 0 uvShellIds= 0 0
#    faceArea= 1.5625 1.5625 worldFaceArea= 1.5625 1.5625 uvFaceArea= 0.0625 0.0625
#    boundingBox= X[-2.50,2.50] Y[-0.00,0.00] Z[-2.50,2.50]
#    boundingBoxComponent= X[-2.50,1.25] Y[-0.00,0.00] Z[0.00,2.50]
#    boundingBox2d= U[0.00,1.00] V[0.00,1.00]
#    boundingBoxComponent2d= U[0.00,0.75] V[0.00,0.50]
#    area=25.00 worldArea=25.00 uvArea=1.00

# 精确的 bounding box 数据
cmds.polyCylinder( r=1, h=2, sx=20, sy=1, sz=1, ax=(0, 1, 0), tx=1, ch=1 )
# Result: pCylinder1 polyCylinder1 #

cmds.rotate( 38.340875, 0, 0, r=True, os=True )
cmds.rotate( 0, 0, -36.177835, r=True, os=True )

cmds.polyEvaluate( b=True )
# Result: ((-1.3974823703620598, 1.39748217791327), (-1.7164316223605844, -1.7164316223605844), (-1.6512467204212007, 1.6512465272260637)) #
cmds.polyEvaluate( b=True, ae=True )
# Result: ((-1.3974823951721191, 1.39748215675354), (-1.4071073532104492, -1.4071073532104492), (-1.3598332405090332, 1.3598330020904541)) #

# 地方和世界空间区
cmds.polyCube( w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0, 0, 1), cuv=1, ch=1 )
cmds.setAttr( 'pCube1.scaleY', 2 )
cmds.polyEvaluate( a=True )
# Result: 6
cmds.polyEvaluate( wa=True )
# Result: 10

# UV Shell 信息
cmds.polySphere( sx=20, sy=20 )
cmds.polyAutoProjection()
cmds.hilite()
cmds.select( 'pSphere1.f[282]', 'pSphere1.f[189:192]', replace = True )

#  UV shells的数量
cmds.polyEvaluate( uvShell=True )
# Result: 6

# 可用 UV Shells
cmds.polyEvaluate( activeUVShells=True )
# Result: [1, 4, 5]

# UV shell IDs for selected faces
cmds.polyEvaluate( uvShellIds=True )
# Result: [1, 1, 1, 4, 5]

# UV edge pairs for selected edges
cmds.polyEvaluate( 'pSphere1.e[642]', uvEdgePairs=True )
# Result: [u'pSphereShape1.map[67] pSphereShape1.map[74] pSphereShape1.map[307] pSphereShape1.map[300] ']
