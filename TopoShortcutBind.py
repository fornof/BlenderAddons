bl_info = {
    "name": "ShortcutTool",
    "author": "Robert Fornof",
    "version": (0, 5),
    "blender": (2, 70, 0),
    "location": "Check the shortcuts for dynamic topology ",
    "description": "CTRL +SPACE toggles subdiv edges and collapse edges, hold down Q in sculpt to do the same",
    "warning": "",
    "wiki_url": "",
    "category": "Object"}
import bpy
from bpy.app.handlers import persistent


def Press(self,context):
    c = 'COLLAPSE'
    context.tool_settings.sculpt.detail_refine_method = c
    print("Pressed")
    
def Release(self,context):
    s = 'SUBDIVIDE'
    c = 'COLLAPSE'
    context.tool_settings.sculpt.detail_refine_method = s
    print("Released")
   
def Toggle(self,context):
    s = 'SUBDIVIDE'
    c = 'COLLAPSE'
    context = bpy.context.scene
    currentSetting = context.tool_settings.sculpt.detail_refine_method
    if currentSetting == s:
        context.tool_settings.sculpt.detail_refine_method = c
        
    elif currentSetting == c:
        context.tool_settings.sculpt.detail_refine_method = s

    else:
        context.tool_settings.sculpt.detail_refine_method = s #default


class TopoShortcutOn(bpy.types.Operator):
    """This Operator Add a Object to Another with Boolean Operations"""
    bl_idname = "object.collapseon"
    bl_label = "Topo Subdiv Toggle"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        print("Toggled")
        Release(self,context)
        
        return {'FINISHED'}


class TopoShortcutToggle(bpy.types.Operator):
    """This Operator Add a Object to Another with Boolean Operations"""
    bl_idname = "object.collapseon"
    bl_label = "Topo Subdiv Toggle"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        print("Toggled")
        Toggle(self,context)
        
        return {'FINISHED'}
    
class TopoShortcutOff(bpy.types.Operator):
    """This Operator Add a Object to Another with Boolean Operations"""
    bl_idname = "object.collapseon"
    bl_label = "Topo Subdiv Toggle"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        print("Toggled")
        Release(self,context)
        
        return {'FINISHED'}

def setTool(input):
    context.tool_settings.sculpt.detail_refine_method = input
 
 #------------------- REGISTER ------------------------------      
addon_keymaps = []

def register():

    bpy.utils.register_class(TopoShortcutOff)
    bpy.utils.register_class(TopoShortcutOn)
    bpy.utils.register_class(TopoShortcutToggle)
    km = bpy.context.window_manager.keyconfigs.active.keymaps['Sculpt']
    kmi = km.keymap_items.new(TopoShortcutOff.bl_idname, 'Q', 'PRESS', ctrl = False)
    kmi = km.keymap_items.new(TopoShortcutOn.bl_idname, 'Q', 'RELEASE', ctrl = False)
    kmi = km.keymap_items.new(TopoShortcutToggle.bl_idname, 'SPACE', 'RELEASE', ctrl = True)

def unregister():
    
    bpy.utils.unregister_class(TopoShortcutOff)
    bpy.utils.unregister_class(TopoShortcutOn)
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    

if __name__ == "__main__":
    register()

 

