#Blender - versão sugerida 2.79b

### Veja a gravação de nossa aula (disponível no AVA e chat do Teams)


### Atividade 1 - Excluir objetos utilizando scripting python

*No paimel do Blender busque pelo item na barra de ferramentas "Choose screen layout selecionar scripting"*

```
import bpy
bpy.data.objects['Cube'].select =True
bpy.ops.object.delete()
```

a. Descreva as mudanças ocorrido em tua tela após a inserção deste script python no Blender.
b. Cite um outro exemplo disponível na documentação oficial do bpy (biblioteca proprietária do blender) para o início de seu aprendizado em python utilizando blender.


### Atividade 2 - Criar esferas e cubos utilizando scripting python

```
import bpy

for i in range (-9, 10, 3):
    bpy.ops.mesh.primitive_cube_add(location=(i,0,0))
    bpy.ops.mesh.primitive_uv_sphere_add(location=(i,0,3))
```
a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas neste script.

### Atividade 3 - Limpar objetos na tela (scripting python)

import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas neste script.

### Atividade 4 - Criar materiais e apectos utilizando scripting python
a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas nos testes de script abaixo.

**Teste com materials - smooth**

```
import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_smooth()
esfera1= bpy.context.object
```

**Teste com materials - flat**

```
import bpy

bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,2))
bpy.ops.object.shade_flat()
esfera1= bpy.context.object
```
### Atividade 5 - Criar materiais e apectos personalizados utilizando scripting python
a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas nos testes de script abaixo.

```
import bpy

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
```
### Atividade 6 - Animação - etapa 1
a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas nos testes de script abaixo.
```
import bpy

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
```

### Atividade 7 - Animação - etapa 2 (cena com animação)
a. Conforme disponível na documentação oficial do bpy comente sobre as estruturas utilizadas nos testes de script abaixo.

```
import bpy

cena=bpy.context.scene
cena.frame_end=50
bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
esfera=bpy.context.object

locations=[(0,0,-2),(0,0,-1),(0,0,0),(0,0,1),(0,0,2))]
quadro=0

for l in locations:
    cena.frame_set(quadro)
    esfera.location = l
    esfera.keyframe_insert(data_path='location')
    quadro +=40