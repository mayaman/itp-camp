import bpy
for i in range(5):
    for j in range(5):
        for k in range(5):
            bpy.ops.mesh.primitive_cube_add(location=(i * 3, j * 3, k * 3))
            
            
