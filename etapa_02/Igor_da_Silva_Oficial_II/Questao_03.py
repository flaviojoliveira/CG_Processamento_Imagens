import bpy
from bpy_extras import view3d_utils
from mathutils import Vector
from bpy.props import BoolProperty
import rna_keymap_ui
bl_info = {
    "name": "RayCast Select",
    "location": "View3D > Add > Object > RayCast Select",
    "description": "RayCast Select",
    "author": "Vladislav Kindushov",
    "version": (0, 4),
    "blender": (2, 91, 0),
    "category": "Object",
}
addon_keymaps = []

def PerspOrOrtot():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.region_3d.is_perspective:
                        return False
                    else:
                        
                        return True

class VIEW3D_OT_raycast_selection(bpy.types.Operator):
    """Click and drag to select"""
    bl_idname = "view3d.raycast_selection"
    bl_label = "RayCast Selection"
    bl_options = {'REGISTER', 'UNDO'}

    Deselect: BoolProperty(
        name="Deselect",
        description="",
        default = False,
    )
    Extend: BoolProperty(
        name="Extend",
        description="",
        default = False,
    )

    
    @classmethod
    def poll(cls, context):
        return context.mode in ['EDIT_CURVE', 'OBJECT', 'EDIT_MESH','EDIT_ARMATURE','POSE']

    def modal(self, context, event):


        # get the ray from the viewport and mouse
        if bpy.context.mode == 'OBJECT':
            MousePosition = Vector(((event.mouse_x) - context.area.regions.data.x, event.mouse_y - context.area.regions.data.y))
            region = bpy.context.region
            rv3d = bpy.context.region_data
            view_vector_mouse = view3d_utils.region_2d_to_vector_3d(region, rv3d, MousePosition)
            ray_origin_mouse = view3d_utils.region_2d_to_origin_3d(region, rv3d, MousePosition)
            direction = ray_origin_mouse + (view_vector_mouse * 1000)
            direction =  direction - ray_origin_mouse
            result, location, normal, index, obj, matrix = bpy.context.scene.ray_cast(bpy.context.view_layer.depsgraph, ray_origin_mouse, direction)
            
            if result:
                if self.Extend and not obj.select_get():
                    bpy.ops.view3d.select('INVOKE_DEFAULT', extend=True, deselect=False)
                elif self.Deselect and obj.select_get():
                    obj.select_set(False)
                elif not self.Extend and not self.Deselect and not obj.select_get():
                    bpy.ops.view3d.select('INVOKE_DEFAULT', extend=True, deselect=False)

        else:# context.mode in ['EDIT_CURVE','EDIT_MESH']:
            if self.Extend:
                bpy.ops.view3d.select('INVOKE_DEFAULT', extend=True, deselect=False)
            elif self.Deselect:
                bpy.ops.view3d.select('INVOKE_DEFAULT', extend=False, deselect=True)
            elif not self.Extend and not self.Deselect:
                bpy.ops.view3d.select('INVOKE_DEFAULT', extend=True, deselect=False)
        # elif context.mode == 'EDIT_ARMATURE':
        #     self.obj =

        if event.value == 'RELEASE':
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.space_data.type == 'VIEW_3D':
            if not self.Extend and not self.Deselect: 
                if  context.mode == 'EDIT_MESH':
                    bpy.ops.mesh.select_all(action='DESELECT')
                if  context.mode == 'EDIT_CURVE':
                    bpy.ops.curve.select_all(action='DESELECT')
                elif context.mode == 'EDIT_ARMATURE':
                    bpy.ops.armature.select_all(action='DESELECT')
                elif context.mode == 'POSE':
                    bpy.ops.pose.select_all(action='DESELECT')
                elif context.mode == 'OBJECT':
                    bpy.ops.object.select_all(action='DESELECT')
                    
            self.obj = context.active_object
            
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            return {'CANCELLED'}

def FindConflict(box, item):
    ku = bpy.context.window_manager.keyconfigs.user
    km = ['3D View','3D View Generic','Object Mode', 'Mesh','Curve','Armature']
    for km_n in km: 
        for i in bpy.context.window_manager.keyconfigs.user.keymaps[km_n].keymap_items:
            if item.type == i.type and item.ctrl == i.ctrl and item.alt == i.alt and item.shift == i.shift and item.name != i.name:
                col = box.column()
                col.label(text='Conflict hotkey: ' + '3D View -> ' + km_n + ' -> ' + i.name + " : ")
                # col.prop(bpy.context.window_manager.keyconfigs.user.keymaps.get(km_n), i)
                rna_keymap_ui.draw_kmi([], ku, bpy.context.window_manager.keyconfigs.user.keymaps[km_n], i, box, 0)
                return None


class raycast_selection_pref(bpy.types.AddonPreferences):
    bl_idname = __name__
    def draw(self, context):
        layout = self.layout
        ConflictBox = layout.row().box()

        HotkeyBox = layout.row().box()

        ku = bpy.context.window_manager.keyconfigs.user
        km = ku.keymaps.get('3D View')
        for i in km.keymap_items:
            if i.idname == "view3d.raycast_selection":
                rna_keymap_ui.draw_kmi([], ku, km, i, HotkeyBox, 0)
                FindConflict(ConflictBox, i)

classes = (VIEW3D_OT_raycast_selection, raycast_selection_pref)

def add_hotkey(prop=None, prop_value=None, shift=False, ctrl=False, alt=False):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = km.keymap_items.new('view3d.raycast_selection', 'MIDDLEMOUSE', 'PRESS', shift=shift, ctrl=ctrl, alt=alt, head=True)

    if not prop is None:
        kmi.properties[prop] = prop_value

    global addon_keymaps
    addon_keymaps.append((km, kmi))

def register():
    for c in classes:
        bpy.utils.register_class(c)

    add_hotkey(prop='Deselect', prop_value=True,shift=False, ctrl=True)
    add_hotkey(prop='Extend', prop_value=True , shift=True, ctrl=False)
    add_hotkey()

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

    for c in reversed(classes):
        bpy.utils.unregister_class(c)

if __name__ == "__main__":
    register()