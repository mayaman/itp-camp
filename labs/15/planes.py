import bpy
import random
def square(name, x, y, z=0):
    verts = [(0,0,z),(2,0,z),(2,2,z),(0,2,z)]
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
        square(str(i) + str(j), i * 2, j * 2, z=random.randint(0,3))
        


