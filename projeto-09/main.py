#Blender


## Atividade 1 - Excluir objetos utilizando scripting python

### No paimel do Blender busque pelo item na barra de ferramentas "Choose screen layout selecionar scripting"

import bpy
bpy.data.objects['Cube'].select =True
bpy.ops.object.delete()


## Atividade 2 - Criar esferas e cubos utilizando scripting python

### Choose screen layout selecionar scripting

import bpy

for i in range (-9, 10, 3):
    bpy.ops.mesh.primitive_cube_add(location=(i,0,0))
    bpy.ops.mesh.primitive_uv_sphere_add(location=(i,0,3))

## Atividade 3 - Limpar objetos na tela (scripting python)

import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()


## Atividade 4 - Criar materiais e apectos utilizando scripting python

### Choose screen layout selecionar scripting

import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object

# teste 2 : Flat

import bpy


bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_flat()
esfera1= bpy.context.object

# teste 3 adicionar esfera manualmente

bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,-1))
esfera2 = bpy.context.object

material=bpy.data.materials.new('brilhante')
material.diffuse_color=(1,0,0)
material.specular_color=(1,0,0)
material.diffuse_intensity=0.8
material.specular_intensity=0.8


# Compilar

import bpy


##nova atividade 6

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,-1))
esfera2 = bpy.context.object

material=bpy.data.materials.new('brilhante')
material.diffuse_color=(1,0,0)
material.specular_color=(1,0,0)
material.diffuse_intensity=0.8
material.specular_intensity=0.8

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,-1))
bpy.ops.object.shade_flat()
esfera2= bpy.context.object

material=bpy.data.materials.new('brilhante')
material.diffuse_color=(1,1,0)
material.specular_color=(1,1,0)
material.diffuse_intensity=0.8
material.specular_intensity=0.8

esfera1.data.materials.append(material)
esfera2.data.materials.append(material)





import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,-1))
bpy.ops.object.shade_flat()
esfera1= bpy.context.object



