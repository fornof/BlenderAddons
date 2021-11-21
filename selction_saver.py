bl_info = {
    "name": "Selection Tool",
    "author": "Robert Fornof",
    "version": (1, 0),
    "blender": (2, 91, 0),
    "location": "View3D > Tool_Tab> Selection",
    "description": "Set selection",
    "warning": "",
    "wiki_url": "",
    "category": "Object"}

import bpy
from bpy.app.handlers import persistent

selected = None

#------------------- FUNCTIONS------------------------------

# Do the Basic Union, Difference and Intersection Operations
def Operation(context,_operation):
    pass
           
#------------------- OPERATOR CLASSES ------------------------------                
# Selection Tool                 



class SelectionSet(bpy.types.Operator):
    """This creates a selection from objects selected"""
    bl_idname = "object.selection_set"
    bl_label = "Selection Save"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def execute(self, context):
        global selected
        selected = bpy.context.selected_objects
        return {'FINISHED'}
    
    
class SelectionGet(bpy.types.Operator):
    """this retrieves selection """
    bl_idname = "object.selection_get"
    bl_label = "Selection Retrieve"

    @classmethod
    def poll(cls, context):
        global selection
        return selected is not None 
    
    def execute(self, context):
        global selected
        for obj in selected: 
            obj.select_set(1)
        return {'FINISHED'}



#------------------- MENU CLASSES ------------------------------  

class SelectionMenu(bpy.types.Menu):
    bl_label = "Selection_Selection_Tool_MT_"
    bl_idname = "OBJECT_MT_selection"

    def draw(self, context):
        layout = self.layout

        self.layout.operator(SelectionTool.bl_idname,icon = "ZOOMIN")
       
class SelectionTab(bpy.types.Panel):
    #"[note]: Add a selection on the x, y , or z axis using : ALT+SHIFT+X , ALT+SHIFT+Y, ALT+SHIFT+Z in object mode"
    bl_label = "Selection"
    bl_idname = "Selection_Selection_Tool_PT_"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Selection"
    bl_context = "objectmode"
    
    def draw(self,context):
        layout = self.layout
        box = layout.box()
        box.label(text="Selection Axis:",icon = "MODIFIER")    
        box.operator(SelectionSet.bl_idname ,icon = "ZOOM_IN")
        box.operator(SelectionGet.bl_idname ,icon = "ZOOM_IN")
        box.separator()  
    #---------- Tree Viewer--------------
def VIEW3D_SelectionMenu(self, context):
    self.layout.menu(SelectionMenu.bl_idname)
    
#------------------- REGISTER ------------------------------      
addon_keymaps = []

def register():

    
    # Operators

    bpy.utils.register_class(SelectionSet)
    bpy.utils.register_class(SelectionGet)
    #bpy.utils.register_class(SelectionZ)
    #Append 3DVIEW Menu
    #bpy.utils.register_class(SelectionMenu)
    #bpy.types.VIEW3D_MT_object.append(VIEW3D_SelectionMenu)
    
    # Append 3DVIEW Tab
    bpy.utils.register_class(SelectionTab)
    
    # handle the keymap
#    wm = bpy.context.window_manager
#    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
#    kmi = km.keymap_items.new(SelectionX.bl_idname, 'X', 'PRESS', alt=True, shift = True)
#    addon_keymaps.append((km, kmi))

#    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
#    kmi = km.keymap_items.new(SelectionY.bl_idname, 'Y', 'PRESS', alt=True, shift = True)
#    addon_keymaps.append((km, kmi))

#    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
#    kmi = km.keymap_items.new(SelectionZ.bl_idname, 'Z', 'PRESS', alt=True, shift = True)
#    addon_keymaps.append((km, kmi))

def unregister():
    
    #bpy.utils.unregister_class(SelectionMenu)
    bpy.utils.unregister_class(SelectionTab)
    #bpy.types.VIEW3D_MT_object.remove(VIEW3D_SelectionMenu)
        
    #Operators
    bpy.utils.unregister_class(SelectionGet)
    bpy.utils.unregister_class(SelectionSet)
#    bpy.utils.unregister_class(SelectionZ)
            
   # bpy.app.handlers.scene_update_post.remove(HandleScene)
    #bpy.types.VIEW3D_MT_object.remove(VIEW3D_SelectionMenu)
    
    # Keymapping
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    

if __name__ == "__main__":
    try:
        unregister()
    except:
        pass
    register()