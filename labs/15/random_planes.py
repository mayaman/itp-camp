import random
import bpy
def square(name, x, y, v1z=0, v2z=0, v3z=0, v4z=0):
    verts = [(0,0,v1z),(1,0,v2z),(1,1,v3z),(0,1,v4z)]
    faces = [[0,1,2,3]]
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name + '_obj', mesh)
    obj.location.x = x
    obj.location.y = y
    bpy.context.scene .objects.link(obj)


for i in range(-4,4):
    for j in range(-4,4):
        square(str(i) + str(j), i * 2, j * 2, v1z=random.randint(0,3), v2z=random.randint(0,3), v3z=random.randint(0,3), v4z=random.randint(0,3))
        


