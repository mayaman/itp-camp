import bpy  

# create a list of vertices - should be a list of 3-element tuples
verts = [(0,0,0),(3,0,0),(2,2,0),(1,1,1)]

# create a list of faces - should be a list of lists, with each inner list representing the index of the element
faces = [[1,2,3],[1,2,4],[1,3,4],[2,3,4]]

# create a new mesh by using bpy.data.meshes.new
triangle_mesh = bpy.data.meshes.new('triangle data')

# define the mesh by using lists of verts and either edges or faces
triangle_mesh.from_pydata(verts, [], faces)

# update mesh with the data that we just defined
triangle_mesh.update()

# create a new object, pass in a name and the data to define it (in this case, the mesh)
triangle_obj = bpy.data.objects.new('triangle_obj', triangle_mesh)

# add the object to the current scene
bpy.context.scene .objects.link(triangle_obj)
