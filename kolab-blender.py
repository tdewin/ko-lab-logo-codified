logo = "kolab"
multiline_str = """
10010001110
10100010001
11000010001
10100010001
10010001110
00000000000
10000100110
10001010101
10001110110
10001010101
11101010110
"""

import bpy

# 1. Create the new collection in data
kollection = bpy.data.collections.new(logo)
bpy.context.scene.collection.children.link(kollection)
bpy.context.view_layer.active_layer_collection = (
    bpy.context.view_layer.layer_collection.children[kollection.name]
)


# Split into lines and strip whitespace from each line
lines = [line.strip() for line in multiline_str.strip().splitlines()]


div=50
wid=10/div
ht=10/div
gap=2/div

xwid = len(lines[0])
yht = len(lines)

totwidth = (xwid)*(wid+gap)-gap
totheight = (yht)*(ht+gap)-gap

print(xwid,yht,totwidth,totheight)

planes = []

for y in range(len(lines)):
 line = lines[y]
 for x in range(len(line)):
  char = line[x]
  if char == "1":
    # plane is 2d/cube is 3d
    #planes.append(bpy.ops.mesh.primitive_plane_add(size=wid, location=((wid+gap)*x, (ht+gap)*-y, 0)))
    bpy.ops.mesh.primitive_cube_add(size=wid, location=((wid+gap)*x, (ht+gap)*-y, 0))
  else:
    print(' ',end="")
 print()

bpy.ops.object.select_all(action="DESELECT")
#kollection = bpy.data.collections['kolab']

for plane in kollection.objects:
    plane.select_set(True)

bpy.ops.object.join()
bpy.context.active_object.name = f"{logo}-logo"
bpy.context.scene.cursor.location[0] = totwidth/2
bpy.context.scene.cursor.location[1] = -totheight/2
bpy.context.scene.cursor.location[2] = 0

bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')


