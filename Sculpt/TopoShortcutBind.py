bl_info = {
    "name": "ShortcutTool",
    "author": "Robert Fornof",
    "version": (0, 1),
    "blender": (2, 70, 0),
    "location": "Check the shortcuts for dynamic topology ",
    "description": "CTRL +SPACE toggles subdiv edges and collapse edges",
    "warning": "",
    "wiki_url": "",
    "category": "Object"}
import bpy
from bpy.app.handlers import persistent

s = 'SUBDIVIDE'
c = 'COLLAPSE'
context = bpy.context.scene

def Toggle():
    currentSetting = context.tool_settings.sculpt.detail_refine_method
    if currentSetting == s:
        context.tool_settings.sculpt.detail_refine_method = c
        
    elif currentSetting == c:
        context.tool_settings.sculpt.detail_refine_method = s

    else:
        context.tool_settings.sculpt.detail_refine_method = s #default


class TopoShortcut(bpy.types.Operator):
    """This Operator Add a Object to Another with Boolean Operations"""
    bl_idname = "object.subdiv"
    bl_label = "Topo Subdiv Toggle"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        print("Toggled")
        Toggle()
        print("Toggled")
        return {'FINISHED'}
    
    

def setTool(input):
    context.tool_settings.sculpt.detail_refine_method = input
 
 #------------------- REGISTER ------------------------------      
addon_keymaps = []

def register():

    bpy.utils.register_class(TopoShortcut)
 
    km = bpy.context.window_manager.keyconfigs.active.keymaps['Sculpt']
    kmi = km.keymap_items.new(TopoShortcut.bl_idname, 'SPACE', 'PRESS', ctrl = True)


def unregister():
    
    bpy.utils.unregister_class(TopoShortcut)

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    

if __name__ == "__main__":
    register()

 